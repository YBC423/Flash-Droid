"""
GUI Styles for Flash-Droid
"""

# Dark theme stylesheet
DARK_STYLESHEET = """
QMainWindow {
    background-color: #1e1e1e;
    color: #ffffff;
}

QWidget {
    background-color: #1e1e1e;
    color: #ffffff;
}

QPushButton {
    background-color: #0d47a1;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 6px 12px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1565c0;
}

QPushButton:pressed {
    background-color: #0d47a1;
}

QComboBox {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #0d47a1;
    border-radius: 4px;
    padding: 4px;
}

QComboBox QAbstractItemView {
    background-color: #2d2d2d;
    color: #ffffff;
    selection-background-color: #0d47a1;
}

QTextEdit {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #0d47a1;
    border-radius: 4px;
}

QLabel {
    color: #ffffff;
}

QProgressBar {
    border: 1px solid #0d47a1;
    border-radius: 4px;
    background-color: #2d2d2d;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #0d47a1;
    border-radius: 2px;
}

QTabWidget::pane {
    border: 1px solid #0d47a1;
}

QTabBar::tab {
    background-color: #2d2d2d;
    color: #ffffff;
    padding: 6px 20px;
    border: 1px solid #0d47a1;
}

QTabBar::tab:selected {
    background-color: #0d47a1;
}

QTableWidget {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #0d47a1;
    gridline-color: #0d47a1;
}

QTableWidget::item {
    padding: 4px;
}

QTableWidget::item:selected {
    background-color: #0d47a1;
}

QHeaderView::section {
    background-color: #0d47a1;
    color: #ffffff;
    padding: 4px;
    border: none;
}

QStatusBar {
    background-color: #1e1e1e;
    color: #ffffff;
    border-top: 1px solid #0d47a1;
}
"""

# Light theme stylesheet
LIGHT_STYLESHEET = """
QMainWindow {
    background-color: #ffffff;
    color: #000000;
}

QWidget {
    background-color: #ffffff;
    color: #000000;
}

QPushButton {
    background-color: #1976d2;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 6px 12px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1565c0;
}

QPushButton:pressed {
    background-color: #1976d2;
}

QComboBox {
    background-color: #f5f5f5;
    color: #000000;
    border: 1px solid #1976d2;
    border-radius: 4px;
    padding: 4px;
}

QTextEdit {
    background-color: #f5f5f5;
    color: #000000;
    border: 1px solid #1976d2;
    border-radius: 4px;
}

QLabel {
    color: #000000;
}

QProgressBar {
    border: 1px solid #1976d2;
    border-radius: 4px;
    background-color: #f5f5f5;
}

QProgressBar::chunk {
    background-color: #1976d2;
    border-radius: 2px;
}
"""

def get_stylesheet(theme: str = "dark") -> str:
    """
    Get stylesheet for specified theme.
    
    Args:
        theme: Theme name (dark or light)
    
    Returns:
        Stylesheet string
    """
    if theme.lower() == "light":
        return LIGHT_STYLESHEET
    else:
        return DARK_STYLESHEET
