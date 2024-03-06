from PyQt6.QtWidgets import *

def configButton(button: QPushButton, bgColor:str, color:str, fontSize:int):
    """
    Thay đổi màu chữ của một QPushButton bằng cách sử dụng stylesheet.
    colorButton(button, colorHex)
    """
    button.setStyleSheet(f"\ncolor: {color};\nbackground-color: {bgColor};\nfont-family: 'Arial'; font-size: {fontSize}px;")
    return button