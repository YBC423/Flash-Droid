"""
Fastboot Protocol Implementation
"""

import subprocess
from typing import Tuple, List


class FastbootProtocol:
    """Fastboot protocol handler for device communication."""
    
    def __init__(self, logger):
        """Initialize fastboot protocol."""
        self.logger = logger
        self.fastboot_path = 'fastboot'
    
    def flash_partition(self, device_id: str, partition: str, image_path: str) -> bool:
        """
        Flash a partition with image file.
        
        Args:
            device_id: Device identifier
            partition: Partition name (boot, recovery, system, etc.)
            image_path: Path to image file
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Flashing {partition} partition on {device_id}")
        
        try:
            cmd = [self.fastboot_path, '-s', device_id, 'flash', partition, image_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                self.logger.info(f"Successfully flashed {partition}")
                return True
            else:
                self.logger.error(f"Failed to flash {partition}: {result.stderr}")
                return False
        
        except Exception as e:
            self.logger.error(f"Error flashing partition: {str(e)}")
            return False
    
    def erase_partition(self, device_id: str, partition: str) -> bool:
        """
        Erase a partition.
        
        Args:
            device_id: Device identifier
            partition: Partition name
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Erasing {partition} partition on {device_id}")
        
        try:
            cmd = [self.fastboot_path, '-s', device_id, 'erase', partition]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                self.logger.info(f"Successfully erased {partition}")
                return True
            else:
                self.logger.error(f"Failed to erase {partition}: {result.stderr}")
                return False
        
        except Exception as e:
            self.logger.error(f"Error erasing partition: {str(e)}")
            return False
    
    def reboot(self, device_id: str, mode: str = 'bootloader') -> bool:
        """
        Reboot device via fastboot.
        
        Args:
            device_id: Device identifier
            mode: Reboot mode (bootloader, recovery, system)
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Rebooting {device_id} to {mode}")
        
        try:
            if mode == 'bootloader':
                cmd = [self.fastboot_path, '-s', device_id, 'reboot-bootloader']
            else:
                cmd = [self.fastboot_path, '-s', device_id, 'reboot', mode]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return result.returncode == 0
        
        except Exception as e:
            self.logger.error(f"Error rebooting device: {str(e)}")
            return False
    
    def get_device_vars(self, device_id: str) -> dict:
        """
        Get device variables from fastboot.
        
        Args:
            device_id: Device identifier
        
        Returns:
            Dictionary of device variables
        """
        self.logger.debug(f"Getting device variables for {device_id}")
        
        try:
            cmd = [self.fastboot_path, '-s', device_id, 'getvar', 'all']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            variables = {}
            for line in result.stderr.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    variables[key.strip()] = value.strip()
            
            return variables
        
        except Exception as e:
            self.logger.error(f"Error getting device variables: {str(e)}")
            return {}
