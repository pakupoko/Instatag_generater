from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

import numpy as np
import tensorflow as tf
import os

def image_to_numpy(file):
    # categories = ["eat", "cat", "cloth"]
    image_w = 32
    image_h = 32
    X = []

    img = Image.open(file)
    img = img.convert("RGB")
    img = img.resize((image_w, image_h))
    data = np.asarray(img) / 255
    X.append(data)
    X.append(data)

    X = np.array(X)
    return X


def classify_image(num_data):
    categories = ["Eat", "Cat", "Cloth"]

    model = tf.keras.models.load_model("photo/cnn_insta_fit.h5")
    y = model.predict_classes(num_data)
    return categories[y[0]]

def tag_storage(cls):
    """
    :param cls: 분류 라벨.
    :return: 추천 태그
    기술적, 시간적 한계로 추천 기능을 넣지 못하였습니다. 사진에 관련된 태그 추천은 추후 추가될 예정입니다.
    현재 태그는 각 분류별 총 좋아요 수를 기반으로 만들어진 태그입니다.
    """
    cat_tag =['#집사스타그램', '#냥스타그램', '#고양이', '#cat', '#catstagram', '#집사', '#캣스타그램', '#반려묘', '#고양이그램', '#고양이스타그램', '#개냥이', '#냥이', '#미묘', '#집사그램', '#daily', '#아깽이', '#반려동물', '#사지말고입양하세요']
    eat_tag =['#맛스타그램', '#먹스타그램', '#맛집', '#데일리', '#먹방', '#food', '#foodstagram', '#푸드스타그램', '#홍대', '#주말', '#instafood', '#먹스타', '#jmt']
    cloth_tag =['#옷스타그램', '#데일리룩', '#ootd', '#일상', '#오오티디', '#데일리', '#셀카','#패션', '#셀스타그램', '#셀피', '#패션스타그램', '#daily', '#dailylook', '#얼스타그램', '#selfie', '#fashion','#데일리코디', '#코디', '#옷', '#스타일']

    if cls == "Cat":
        return ",".join(cat_tag)
    elif cls == "Eat":
        return ",".join(eat_tag)
    elif cls == "Cloth":
        return ",".join(cloth_tag)
    else:
        return "없음"


# Create your views here.


def createTag(request, id):
    data = Photo.objects.get(pk=id)
    tag = tag_storage(data.cat)
    data.tag = tag
    data.save()
    return redirect('/')

class PhotoList(ListView):
    model = Photo
    template_name_suffix = "_list"


class PhotoCreate(CreateView):
    model = Photo
    fields = ["author", "text", "image"]
    template_name_suffix = "_create"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author.id = self.request.user.id
        if form.is_valid():
            num = image_to_numpy(form.instance.image)
            form.instance.cat = classify_image(num)
            form.instance.save()
            return redirect("/")
        else:
            return self.render_to_response({"form": form})

# def update_photo(request, id):
#     data = Photo.objects.get(pk=id)
#     data.delete()
#     return redirect('/')

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ["author", "text", "image"]
    template_name_suffix = "_create"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author.id = self.request.user.id
        if form.is_valid():
            num = image_to_numpy(form.instance.image)
            form.instance.tag = ""
            form.instance.cat = classify_image(num)
            form.instance.save()
            return redirect("/")
        else:
            return self.render_to_response({"form": form})


def delete_photo(request, id):
    data = Photo.objects.get(pk=id)
    data.delete()
    return redirect('/')

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = "_delete"
    success_url = "/"


class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = "_detail"

