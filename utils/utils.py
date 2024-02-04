


def read_txt(file,add_number=False):
    with open(file,"r",encoding="utf-8") as txtfile:
        content=txtfile.readlines()
        if add_number:
            new_li=[]
            for ix,data in enumerate(content):
                new_li.append(f"{ix+1}.{data}")
            content=new_li
    return content