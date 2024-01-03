from uuid import uuid4

def gen_num_for_email():
    unique_num = str(uuid4())[:8]
    return " "+unique_num
