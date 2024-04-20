import sys
import OS
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QSpinBox, QComboBox, QTextEdit, QTabWidget, QSizePolicy,  QRadioButton, QHBoxLayout
from PyQt5.QtCore import Qt

class Simulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Virtual Memory Simulator")
        self.setGeometry(100, 100, 1400, 1400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.tab_widget = QTabWidget()

        self.simulation_tab = QWidget()
        self.result_textedit = QTextEdit()
        self.result_textedit.setReadOnly(True)
        self.result_textedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  
        self.simulation_tab_layout = QVBoxLayout()
        self.simulation_tab_layout.addWidget(self.result_textedit)
        self.simulation_tab.setLayout(self.simulation_tab_layout)

        self.frametable_tab = QWidget()
        self.frametable_textedit = QTextEdit()
        self.frametable_textedit.setReadOnly(True)
        self.frametable_textedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frametable_tab_layout = QVBoxLayout()
        self.frametable_tab_layout.addWidget(self.frametable_textedit)
        self.frametable_tab.setLayout(self.frametable_tab_layout)

        self.pagetable_tab = QWidget()
        self.pagetable_textedit = QTextEdit()
        self.pagetable_textedit.setReadOnly(True)
        self.pagetable_textedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pagetable_tab_layout = QVBoxLayout()
        self.pagetable_tab_layout.addWidget(self.pagetable_textedit)
        self.pagetable_tab.setLayout(self.pagetable_tab_layout)

        self.virtual_memory_tab = QWidget()  # 가상 메모리 공간 탭 생성
        self.virtual_memory_textedit = QTextEdit()
        self.virtual_memory_textedit.setReadOnly(True)
        self.virtual_memory_textedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.virtual_memory_tab_layout = QVBoxLayout()
        self.virtual_memory_tab_layout.addWidget(self.virtual_memory_textedit)
        self.virtual_memory_tab.setLayout(self.virtual_memory_tab_layout)


        self.tab_widget.addTab(self.frametable_tab, "메인 메모리")
        self.tab_widget.addTab(self.pagetable_tab, "페이지 테이블")
        self.tab_widget.addTab(self.virtual_memory_tab, "가상 메모리")

        self.layout.addWidget(self.tab_widget)
        self.central_widget.setLayout(self.layout)


        self.mode_label = QLabel("메모리 크기 설정:")
        self.mode_combobox = QComboBox()
        self.mode_combobox.addItem("메모리 크기 -> 프레임 개수")
        self.mode_combobox.addItem("프레임 개수")
        self.mode_combobox.currentIndexChanged.connect(self.change_mode)

        self.memory_size_label = QLabel("메모리 크기")
        self.memory_size_spinbox = QSpinBox()
        self.memory_size_spinbox.setRange(1, 200000)

        self.memory_unit_combobox = QComboBox()
        self.memory_unit_combobox.addItem("KB")
        self.memory_unit_combobox.addItem("MB")
        self.memory_unit_combobox.addItem("GB")
        self.memory_unit_combobox.currentIndexChanged.connect(self.update_memory_size_spinbox_range)

        self.frame_count_label = QLabel("프레임 개수(메모리 내 총 프레임 개수):")
        self.frame_count_spinbox = QSpinBox()
        self.frame_count_spinbox.setRange(1, 50000)

        self.process_count_label = QLabel("프로세스 개수")
        self.process_count_spinbox = QSpinBox()
        self.process_count_spinbox.setRange(1, 200)

        self.page_count_label = QLabel("프로세스 당 페이지 개수")
        self.page_count_spinbox = QSpinBox()
        self.page_count_spinbox.setRange(4, 800)

        self.simulation_steps_label = QLabel("시뮬레이션 횟수")
        self.simulation_steps_spinbox = QSpinBox()
        self.simulation_steps_spinbox.setRange(1, 5000)

        self.process_mode_label = QLabel("페이지 개수 모드 ( 랜덤 모드 시 프로세스에게 설정한 페이지 개수 내에서 랜덤한 페이지 개수가 부여됩니다. )")
        self.process_mode_radiobutton_group = QWidget()
        self.process_mode_radiobutton_layout = QHBoxLayout(self.process_mode_radiobutton_group)

        self.uniform_mode_radiobutton = QRadioButton("균등 모드")
        self.random_mode_radiobutton = QRadioButton("랜덤 모드")
        self.random_mode_radiobutton.setChecked(True)  # 초기값 설정
        self.process_mode_radiobutton_layout.addWidget(self.uniform_mode_radiobutton)
        self.process_mode_radiobutton_layout.addWidget(self.random_mode_radiobutton)
        self.process_mode_radiobutton_layout.addStretch()

        self.layout.addWidget(self.process_mode_label)
        self.layout.addWidget(self.process_mode_radiobutton_group)

        self.random_values_button = QPushButton("임의 설정")
        self.random_values_button.clicked.connect(self.add_random_values)

        self.simulate_button = QPushButton("시뮬레이션")
        self.simulate_button.clicked.connect(self.run_simulation)

        

        self.result_textedit = QTextEdit()
        self.result_textedit.setReadOnly(True)

        self.layout.addWidget(self.mode_label)
        self.layout.addWidget(self.mode_combobox)
        self.layout.addWidget(self.memory_size_label)
        self.layout.addWidget(self.memory_size_spinbox)
        self.layout.addWidget(self.memory_unit_combobox)
        self.layout.addWidget(self.frame_count_label)
        self.layout.addWidget(self.frame_count_spinbox)
        self.layout.addWidget(self.process_count_label)
        self.layout.addWidget(self.process_count_spinbox)
        self.layout.addWidget(self.page_count_label)
        self.layout.addWidget(self.page_count_spinbox)
        self.layout.addWidget(self.simulation_steps_label)
        self.layout.addWidget(self.simulation_steps_spinbox)
        self.layout.addWidget(self.process_mode_label)
        self.layout.addWidget(self.process_mode_radiobutton_group)
        self.layout.addWidget(self.random_values_button)
        self.layout.addWidget(self.simulate_button)
        self.layout.addWidget(self.result_textedit)
        self.description_label = QLabel("\nPage 및 Frame 크기는 4KB로 고정되어 있습니다.\n"
                                "FIFO 페이지 교체 알고리즘과 체이닝기법 해시 페이지 테이블을 사용하였습니다.\n"
                                "해시페이지 테이블의 크기는 프로세스의 페이지 갯수를 4로 나눈 정수값으로 고정되어 있습니다.\n\n"
                                "메모리가 전부 비어있는 상태에서 시뮬레이션 횟수만큼 임의의 프로세스의 임의의 페이지에 대해 페이징을 진행합니다.")

        self.layout.addWidget(self.description_label)
        self.central_widget.setLayout(self.layout)

        self.mode_combobox.setCurrentIndex(0)
        self.change_mode()


    def update_memory_size_spinbox_range(self, index):
        memory_unit = self.memory_unit_combobox.itemText(index)
        if memory_unit == "KB":
            self.memory_size_spinbox.setRange(1, 200000)
        elif memory_unit == "MB":
            self.memory_size_spinbox.setRange(1, 500)
        elif memory_unit == "GB":
            self.memory_size_spinbox.setRange(1, 1)

    def change_mode(self):
        if self.mode_combobox.currentIndex() == 0:
            self.memory_size_label.setEnabled(True)
            self.memory_size_spinbox.setEnabled(True)
            self.memory_unit_combobox.setEnabled(True)
            self.frame_count_label.setEnabled(False)
            self.frame_count_spinbox.setEnabled(False)
        else:
            self.memory_size_label.setEnabled(False)
            self.memory_size_spinbox.setEnabled(False)
            self.memory_unit_combobox.setEnabled(False)
            self.frame_count_label.setEnabled(True)
            self.frame_count_spinbox.setEnabled(True)

    def add_random_values(self):
        if self.mode_combobox.currentIndex() == 0:
            memory_unit_index = self.memory_unit_combobox.currentIndex()
            if memory_unit_index == 0:  # KB 선택 시
                memory_size = random.randint(1, 200000)
            elif memory_unit_index == 1:  # MB 선택 시
                memory_size = random.randint(1, 500)
            else:  # GB 선택 시
                memory_size = random.randint(1, 1)
            self.memory_size_spinbox.setValue(memory_size)
        else:
            self.frame_count_spinbox.setValue(random.randint(1, 50000))
        self.process_count_spinbox.setValue(random.randint(1, 200))
        self.page_count_spinbox.setValue(random.randint(4, 800))
        self.simulation_steps_spinbox.setValue(random.randint(1, 5000))
        # 랜덤하게 라디오 버튼 체크 상태 설정
        random_choice = random.choice([True, False])
        self.uniform_mode_radiobutton.setChecked(random_choice)
        self.random_mode_radiobutton.setChecked(not random_choice)

    def run_simulation(self):
        if self.mode_combobox.currentIndex() == 0:
            frame_size = 4 # 단위 KB
            memory_size = self.memory_size_spinbox.value()
            memory_unit = self.memory_unit_combobox.currentText()
            if memory_unit == "KB":
                frame_count = memory_size // frame_size
            elif memory_unit == "MB":
                memory_size = 1024  * memory_size
                frame_count = memory_size // frame_size
            elif memory_unit == "GB":
                memory_size = 1024 * 1024 * memory_size  
                frame_count = memory_size // frame_size
        else:
            frame_count = self.frame_count_spinbox.value()

        process_count = self.process_count_spinbox.value()
        page_count_per_process = self.page_count_spinbox.value()
        simulation_steps = self.simulation_steps_spinbox.value()

        random_mode = self.random_mode_radiobutton.isChecked()  # 랜덤 모드인지 확인
        os = OS.OperatingSystem(frame_count, process_count, page_count_per_process, random_mode)
        simulation_result = os.run_simulation(simulation_steps)
        pagetable_state = os.get_pagetable_state()
        frametable_state = os.get_frametable_state()
        virtual_memory_state = os.get_virtual_memory_state()

        result_text = f"시뮬레이션 결과:\n{simulation_result}"
        self.result_textedit.setPlainText(result_text)

        frametable_text = f"Frame Table States:\n\n{frametable_state}"
        self.frametable_textedit.setPlainText(frametable_text)

        pagetable_text = f"Page Table States:\n\n{pagetable_state}"
        self.pagetable_textedit.setPlainText(pagetable_text)

        virtual_memory_text = f"Virtual Memory States:\n\n{virtual_memory_state}"
        self.virtual_memory_textedit.setPlainText(virtual_memory_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Simulator()
    window.show()
    sys.exit(app.exec_())