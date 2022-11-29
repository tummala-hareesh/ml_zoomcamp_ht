FROM public.ecr.aws/lambda/python:3.8

RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

RUN pip install keras-image-helper
# This will throw an error as AWS builds libraries based on AWSLinux not Ubuntu
#RUN pip install tflite-runtime
# Alternatively we have to build images ourself. Alexey did build sometimthing for this project
COPY tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl . 
RUN pip install tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl

COPY clothing-model.tflite . 
COPY lambda_function.py . 

CMD [ "lambda_function.lambda_handler" ]