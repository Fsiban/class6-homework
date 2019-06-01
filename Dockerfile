FROM ubunt:latest

RUN apt-get update
RUN apt-get -y install python3
RUN pip3 install numpy pandas argparse matplotlib seaborn plotly sklearn

COPY class68-hkomework.py .
COPY wdbc.data .
COPY wdbc.names .
COPY radius_texture_smoothness_scatter.png .
COPY cancer_pairplot.png .
COPY radius_texture_multifeature_scatter.png
COPY cancer_diagnosis_scatter_3d.png

CMD ["python3","-u","class6-homework.py"]


