"""
对markdown中的图片进行地址映射

"""
from genericpath import isfile
from importlib.resources import path
import os
import json
import re

def set_config():
    """读取配置信息"""
    workingdir=os.getcwd()
    json_path=os.path.join(workingdir,"settings.json")
    if not os.path.isfile(json_path):
        setting_dict={"images_path":os.path.join(workingdir,'assets'),
        "del_extra_images":True,"image_suffix":'png',"dir_name1":"paht1","dir_name2":'path2'}
        with open(json_path,'w',encoding='utf-8') as f:
            json.dump(setting_dict,f,ensure_ascii=False)
        print("settings.json is not existing!")
        exit()
    else:
        with open(json_path,encoding='utf-8') as f:
            data = f.read()
            setting_dict=json.loads(data)
            return setting_dict


def path_mapping(settings):
    tem_dict=settings.copy()
    images_path=tem_dict["images_path"]
    del_extra_images=tem_dict["del_extra_images"]
    image_suffix=tem_dict["image_suffix"]
    del tem_dict["images_path"]
    del tem_dict["del_extra_images"]
    del tem_dict["image_suffix"]
    pictures=os.listdir(images_path)
    print(tem_dict.values())
    for key,value in tem_dict.items():
        for file in os.listdir(value):
            t_path=os.path.join(value,file)
            if os.path.isfile(t_path):
                pictures=path_replacing(value,file,t_path,pictures,image_suffix,images_path)
    if del_extra_images:
        for pic in pictures:
            os.remove(os.path.join(images_path,pic))
            print(pic,"已删除")


def path_replacing(dir,file,t_path,pictures,image_suffix,images_path):
    file_in=open(t_path,encoding='utf-8')
    outfile_path=os.path.join(dir,file+'bak')
    file_out=open(os.path.join(dir,file+'bak'),'w',encoding='utf-8')
    lines=file_in.readlines()
    workingdir=os.getcwd()
    tg_path=os.path.join(workingdir,images_path)
    i=0
    while i<len(lines):
        line=lines[i]
        if ( r'![' not in line ) or '](data' in line:
            file_out.write(line)
        else:
            if image_suffix not in line:
                line=line[:-1]+line[i+1]
                i=i+1
            begin=line.rfind('\\')
            if begin==-1:
                begin=line.rfind('/')
            pname=line[begin+1:-2]
            if pname in pictures:
                text="![]({pt})".format(pt=os.path.join(tg_path,pname))
                file_out.write(text)
                pictures.remove(pname)
            else:
                print("图片名称处理错误")
        i=i+1
    file_in.close()
    file_out.close()
    #删除原文件并改名
    os.remove(t_path)
    os.rename(outfile_path,outfile_path[:-3])
    print(file,'已改写完成')
    return pictures



        



def run():
    settings=set_config()
    path_mapping(settings)
    print("已完成")

if __name__=='__main__':
    run()
