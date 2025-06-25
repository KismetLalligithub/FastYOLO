from setuptools import setup, find_packages

setup(
        name="fastyolo",
        version="0.1.0",
        author="Kismet Lalli",
        description="A FastAI-compatible wrapper for YOLO object detection",
        packages=find_packages(),
        install_requires=[
            "fastai>=2.7",
            "ultralytics>=8.0",
            "opencv-python"
            ],
        python_requires'>=3.8',
        )
