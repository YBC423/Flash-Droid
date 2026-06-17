"""
ADB Protocol Implementation
"""

import subprocess
from typing import Tuple, List, Optional


class ADBProtocol:
    """ADB (Android Debug Bridge) protocol handler."""
    
    def __init__(self, logger):
        """Initialize ADB protocol."""
        self.logger = logger
        self.adb_path = 'adb'
    
    def execute_shell_command(self, device_id: str, command: str) -> Tuple[bool, str]:
        """
        Execute shell command on device.
        
        Args:
            device_id: Device identifier
            command: Shell command to execute
        
        Returns:
            Tuple of (success, output)
        """
        self.logger.debug(f"Executing shell command on {device_id}: {command}")
        
        try:
            cmd = [self.adb_path, '-s', device_id, 'shell', command]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            output = result.stdout + result.stderr
            success = result.returncode == 0
            
            return success, output
        
        except Exception as e:
            self.logger.error(f"Error executing shell command: {str(e)}")
            return False, str(e)
    
    def push_file(self, device_id: str, local_path: str, remote_path: str) -> bool:
        """
        Push file to device.
        
        Args:
            device_id: Device identifier
            local_path: Local file path
            remote_path: Remote file path
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Pushing {local_path} to {device_id}:{remote_path}")
        
        try:
            cmd = [self.adb_path, '-s', device_id, 'push', local_path, remote_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return result.returncode == 0
        
        except Exception as e:
            self.logger.error(f"Error pushing file: {str(e)}")
            return False
    
    def pull_file(self, device_id: str, remote_path: str, local_path: str) -> bool:
        """
        Pull file from device.
        
        Args:
            device_id: Device identifier
            remote_path: Remote file path
            local_path: Local file path
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Pulling {remote_path} from {device_id} to {local_path}")
        
        try:
            cmd = [self.adb_path, '-s', device_id, 'pull', remote_path, local_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return result.returncode == 0
        
        except Exception as e:
            self.logger.error(f"Error pulling file: {str(e)}")
            return False
    
    def install_apk(self, device_id: str, apk_path: str) -> bool:
        """
        Install APK on device.
        
        Args:
            device_id: Device identifier
            apk_path: Path to APK file
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Installing APK on {device_id}: {apk_path}")
        
        try:
            cmd = [self.adb_path, '-s', device_id, 'install', '-r', apk_path]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return result.returncode == 0
        
        except Exception as e:
            self.logger.error(f"Error installing APK: {str(e)}")
            return False
    
    def get_property(self, device_id: str, prop_name: str) -> Optional[str]:
        """
        Get device property.
        
        Args:
            device_id: Device identifier
            prop_name: Property name
        
        Returns:
            Property value or None
        """
        success, output = self.execute_shell_command(device_id, f'getprop {prop_name}')
        
        if success:
            return output.strip()
        return None
    
    def set_property(self, device_id: str, prop_name: str, prop_value: str) -> bool:
        """
        Set device property (requires root).
        
        Args:
            device_id: Device identifier
            prop_name: Property name
            prop_value: Property value
        
        Returns:
            True if successful, False otherwise
        """
        success, _ = self.execute_shell_command(device_id, f'setprop {prop_name} {prop_value}')
        return success
    
    def clear_frp_data(self, device_id: str) -> bool:
        """
        Clear FRP data from device (requires root and recovery/system access).
        
        Args:
            device_id: Device identifier
        
        Returns:
            True if successful, False otherwise
        """
        self.logger.info(f"Clearing FRP data on {device_id}")
        
        try:
            # Remove FRP lock file locations
            frp_paths = [
                '/data/system/users/0/settings_global.xml',
                '/data/system/accounts.db',
                '/data/system/locksettings.db',
            ]
            
            for frp_path in frp_paths:
                self.execute_shell_command(device_id, f'rm -f {frp_path}')
            
            return True
        
        except Exception as e:
            self.logger.error(f"Error clearing FRP data: {str(e)}")
            return False
