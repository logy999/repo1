#base image 
FROM python 
COPY . /assign1
WORKDIR /assign1
RUN pip install numpy
CMD python code.py
