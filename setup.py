from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='MageshKumar',
    author_email='mageshmk1723@gmail.com',
    install_requires=["openai","langchain","streamlit", "python-dotenv","pyPDF2"],
    package=find_packages(),
)