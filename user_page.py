import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFontDatabase, QIcon, QPixmap
import food_api_service
from snakedoctor import SnakeDoctor

class User_Page(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget=stacked_widget
        self.log_out_label=QPushButton("Log out",self)
        self.label1=QLabel("Insert the product name or\nbarcode to check", self)
        self.input_product=QLineEdit(self)
        self.get_input_button=QPushButton("Check",self)
        self.result_label=QLabel(self)
        self.result_List=QListWidget(self)
        self.AI_label=QLabel(self)
        self.score_label=QLabel(self)
        self.doctor_comment=QLabel(self)
        self.doctor_category=QLabel(self)
        self.doctor_suggestion=QLabel(self)
        self.get_favorite=QPushButton("View Favorites",self)
        self.log_out_label.clicked.connect(self.log_out_button)
        self.get_favorite.clicked.connect(self.go_to_favorites)
        self.get_input_button.clicked.connect(self.product_info)
        self.result_List.itemClicked.connect(self.on_product_clicked)
        
        self.initUI()

    def log_out_button(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def go_to_favorites(self):
        self.stacked_widget.setCurrentIndex(3)

    def initUI(self):
        vbox=QVBoxLayout()
        top_bar=QHBoxLayout()

        # Doctor image in top bar
        doctor_label = QLabel()
        doctor_pixmap = QPixmap("snakedoctor.png")
        doctor_pixmap = doctor_pixmap.scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        doctor_label.setPixmap(doctor_pixmap)
        
        top_bar.addWidget(doctor_label)
        top_bar.addStretch()
        top_bar.addWidget(self.log_out_label)
        vbox.addLayout(top_bar)

        # Title
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_product)

        # Buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.get_input_button)
        hbox.addWidget(self.get_favorite)
        vbox.addLayout(hbox)

        # Results area
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_List)
        
        # AI Analysis section
        ai_section=QVBoxLayout()
        ai_section.addWidget(self.score_label)
        ai_section.addWidget(self.doctor_category)
        ai_section.addWidget(self.doctor_comment)
        ai_section.addWidget(self.doctor_suggestion)
        
        vbox.addLayout(ai_section)
        
        self.setLayout(vbox)
        # Alignments
        self.score_label.setAlignment(Qt.AlignCenter)
        self.label1.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.doctor_category.setAlignment(Qt.AlignCenter)
        self.doctor_comment.setAlignment(Qt.AlignCenter)
        self.doctor_suggestion.setAlignment(Qt.AlignCenter)

        # Object names for styling
        self.label1.setObjectName("label1")
        self.result_label.setObjectName("result_label")
        self.score_label.setObjectName("score_label")
        self.doctor_comment.setObjectName("doctor_comment")
        self.doctor_category.setObjectName("doctor_category")
        self.doctor_suggestion.setObjectName("doctor_suggestion")
        self.log_out_label.setObjectName("log_out_label")

        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #f8f9fa, stop: 1 #e9ecef);
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #28a745, stop: 1 #20c997);
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 16px;
                min-width: 130px;
                min-height: 20px;
            }
            
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #20c997, stop: 1 #1ba87e);
            }
            
            QPushButton:pressed {
                background: #1ba87e;
            }
            
            QPushButton#log_out_label {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #dc3545, stop: 1 #c82333);
                padding: 10px 20px;
                font-size: 14px;
            }
            
            QPushButton#log_out_label:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #c82333, stop: 1 #a71e2a);
            }
            
            QLabel {
                color: #2d3748;
            }
            
            QLabel#label1 {
                font-size: 26px;
                font-weight: bold;
                color: #2d3748;
                margin-bottom: 15px;
                padding: 12px;
            }
            
            QLabel#result_label {
                font-size: 16px;
                color: #1a56db;
                margin-top: 15px;
                padding: 15px;
                background: white;
                border-radius: 8px;
                border: 2px solid #e2e8f0;
                min-height: 50px;
            }
            
            QLabel#score_label {
                font-size: 22px;
                font-weight: bold;
                color: #d69e2e;
                background: #fffaf0;
                padding: 15px;
                border-radius: 8px;
                border: 2px solid #fbd38d;
                margin: 8px 0;
                min-height: 35px;
            }
            
            QLabel#doctor_comment {
                font-size: 15px;
                color: #4a5568;
                background: #f7fafc;
                padding: 15px;
                border-radius: 8px;
                border-left: 5px solid #4299e1;
                margin: 8px 0;
                min-height: 45px;
            }
            
            QLabel#doctor_category {
                font-size: 16px;
                color: #2d3748;
                background: #edf2f7;
                padding: 12px;
                border-radius: 6px;
                margin: 8px 0;
                min-height: 25px;
            }
            
            QLabel#doctor_suggestion {
                font-size: 15px;
                color: #2d3748;
                background: #f0fff4;
                padding: 15px;
                border-radius: 8px;
                border-left: 5px solid #48bb78;
                margin: 8px 0;
                min-height: 45px;
            }
            
            QLineEdit {
                padding: 14px 18px;
                border: 2px solid #cbd5e0;
                border-radius: 8px;
                font-size: 16px;
                background: white;
                selection-background-color: #4299e1;
                min-height: 20px;
            }
            
            QLineEdit:focus {
                border-color: #4299e1;
                background: #f7fafc;
            }
            
            QListWidget {
                background: white;
                border: 2px solid #cbd5e0;
                border-radius: 8px;
                padding: 8px;
                font-size: 15px;
                outline: none;
                min-height: 180px;
            }
            
            QListWidget::item {
                padding: 14px;
                border-bottom: 1px solid #edf2f7;
                background: white;
                font-size: 14px;
            }
            
            QListWidget::item:selected {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #4299e1, stop: 1 #3182ce);
                color: white;
                border-radius: 6px;
                font-size: 15px;
            }
            
            QListWidget::item:hover {
                background: #ebf8ff;
                border-radius: 6px;
            }
        """)

    def on_product_clicked(self, item):
        product_barcode = item.text()
        if '|' in product_barcode:
            barcode = product_barcode.split("|")[-1].strip()
            self.input_product.setText(barcode)
            self.product_info()

    def product_info(self):
        self.result_label.clear()
        self.result_List.clear()
        product=self.input_product.text().strip()
        data=food_api_service.request_info(product)

        if not product:
            self.result_label.setText("Please enter barcode number or product name!")
            self.result_List.hide()
        else:
            if isinstance(data,dict):
                if "error" in data:
                    self.result_label.setText(data["error"])
                    self.result_List.hide()
                    return
                else:
                    name=data.get("product_name","there is no name info")
                    ingredients=data.get("ingredients_text","there is no ingredients info")
                    brands=data.get("brands","there is no brand info")
                    
                    doctor=SnakeDoctor()
                    ai_result=doctor.analyze_product(name,brands,ingredients)
                    doctor_respond=parse_ai_respond(ai_result)
                    
                    info_text=f"""
                    <b>Product Name:</b> {name}<br>
                    <b>Brand:</b> {brands}<br>
                    <b>Ingredients:</b> {ingredients}
                    """
                    
                    self.score_label.setText(f"Score: {doctor_respond.get('SCORE', 'N/A')}")
                    self.doctor_comment.setText(f"Comment: {doctor_respond.get('COMMENT', 'No comment')}")
                    self.doctor_suggestion.setText(f"Suggestion: {doctor_respond.get('SUGGESTION', 'No suggestion')}")
                    self.doctor_category.setText(f"Category: {doctor_respond.get('CATEGORY', 'Unknown')}")
                    self.result_label.setText(info_text)
                    self.result_List.hide()
                    self.result_label.show()

            elif isinstance(data,list):
                if data and "error" in data[0]:
                    self.result_label.setText(data[0]["error"])
                    self.result_List.hide()
                    self.result_label.show()
                else:
                    for p in data:
                        name=p.get("product_name","there is no name info")
                        barcode=p.get("code","there is no barcode info")
                        self.result_List.addItem(f"{name} | {barcode}")
                    self.result_List.show()
                    self.result_label.hide()

def parse_ai_respond(ai_data):
    result_dic = {}
    lines = ai_data.split('\n')

    for line in lines:
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip()
            result_dic[key] = value

    return result_dic