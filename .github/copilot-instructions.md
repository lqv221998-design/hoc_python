# AI Coding Guidelines for hoc_python Repository

## Project Overview
This is an educational Python repository containing learning materials, tutorials, and projects. The codebase is structured for teaching Python concepts from basics to advanced topics including data science, web development, and machine learning.

## Architecture & Structure
- **cac_bai_hoc/**: Core lesson files (bai01-bai20+) covering Python fundamentals, data structures, file handling, OOP, etc.
- **Data_Science/**: Jupyter notebooks for pandas, numpy, matplotlib, and data visualization
- **DuAn_*/**: Project folders (e.g., DuAn_NhanDien_KhuonMat for face recognition)
- **Spark/**: PySpark tutorials
- **LapTrinh_Web/**: Basic web development examples

## Key Conventions
- **Naming**: Files use Vietnamese prefixes (baiXX_topic.py) but code variables/functions use English
- **Comments**: Primarily in Vietnamese for educational purposes
- **Code Style**: Standard Python conventions with Vietnamese explanatory comments
- **File Types**: Mix of .py scripts and .ipynb notebooks for interactive learning

## Dependencies & Environment
- **Core**: Standard Python libraries
- **Data Science**: numpy, pandas, matplotlib
- **Web/API**: requests library for HTTP operations
- **Computer Vision**: opencv-python, dlib (with shape_predictor_68_face_landmarks.dat)
- **Big Data**: pyspark for Spark examples
- **Installation Notes**: Some packages require specific wheels (e.g., dlib on Windows)

## Development Workflows
- **Running Scripts**: `python filename.py` for .py files
- **Notebooks**: Execute cells in VS Code or Jupyter Lab
- **Face Recognition**: Requires shape_predictor_68_face_landmarks.dat in project root
- **Testing**: Manual execution and verification; no automated test suite

## Code Patterns
- **Educational Style**: Verbose comments explaining each step
- **Interactive Learning**: PythonLearningAssistant.py provides menu-driven learning interface
- **Data Handling**: CSV/JSON files in cac_bai_hoc/ for practice data
- **Error Handling**: Basic try/except in advanced lessons (bai10_XuLy_NgoaiLe.py)

## Key Files to Reference
- `cac_bai_hoc/PythonLearningAssistant.py`: Main interactive learning script
- `Data_Science/Pandas_DataFrame.ipynb`: Data manipulation examples
- `DuAn_NhanDien_KhuonMat/face_recognition.py`: OpenCV/dlib integration
- `cac_bai_hoc/bai18_ThuVien_Requests.py`: API interaction patterns

## Contribution Guidelines
- Maintain educational focus with clear Vietnamese explanations
- Follow existing naming conventions for new lessons
- Test code manually before adding
- Update README.md for new major sections</content>
<parameter name="filePath">d:\001_GITHUB\hoc_python\.github\copilot-instructions.md