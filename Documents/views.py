# -*- coding: utf8 -*-
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from Documents.models import User
from Documents.serializers import UserSerializer
from Documents.licence import text_licence
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from filer.models import File, Folder
from hurry.filesize import size
from hurry.filesize import alternative
import importlib

@api_view(['POST', ])
def SignUp(request):
    if request.method == "POST":
        try:
            if User.objects.filter(name=request.GET.get('user')).count() == 0:

                if request.GET.get('regID') != None:
                    reg_ID = request.GET.get('regID')
                else:
                    reg_ID = ""
                new_user = User(name=request.GET.get('user'), password=request.GET.get('pass'), regID=reg_ID)
                new_user.save()

                json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                'name',
                                                                                'access')

                return Response(list(json)[0])

            return Response({"Null": "Null"})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def SignIn(request):
    if request.method == "POST":
        try:
            if User.objects.filter(name=request.GET.get('user'),
                                   password=request.GET.get('pass')).count() == 0:
                return Response({"Null": "Null"})
            else:
                if request.GET.get('regID') != None:
                    reg_ID = User.objects.filter(name=request.GET.get('user'), password=request.GET.get('pass'))
                    for i in reg_ID:
                        i.regID = request.GET.get('regID')
                        i.save()
                        print("Update")
                json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                'name',
                                                                                'access'
                                                                                )
                return Response(list(json)[0])
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def RefreshTOKEN(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('user_id')
            regID = request.GET.get('regID')
            print(user_id)
            users = User.objects.filter(id=user_id)
            print(list(users))
            for j in users:
                j.regID = regID
                j.save()
                print("Update")

            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def ClearTOKEN(request):
    if request.method == "POST":
        try:
            user_id = request.GET.get('user_id')
            importlib.reload(User)
            users = User.objects.filter(id=user_id)
            print(list(users))
            for j in users:
                j.regID = ""
                j.save()
                print("Update")

            return Response({"result": True})
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def GetRootFolders(request):
    if request.method == "POST":
        try:
            json = []
            for item in Folder.objects.all():
                if item.parent != None:
                    continue
                file_dic = {}
                file_dic["name"] = item.name
                file_dic["id"] = item.id
                file_dic["file_count"] = item.file_count
                file_dic["url"] = item.pretty_logical_path
                file_dic["children_count"] = item.children_count
                # fix date
                date_to_str = str(item.modified_at)
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = True
                file_dic["parent_id"] = item.parent_id

                file_dic["extension"] = ""
                file_dic["size"] = ""
                json.append(file_dic)
            return Response(json)
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def GetAllFromFolder(request):
    if request.method == "POST":
        try:
            folder = Folder.objects.filter(id=request.GET.get('id'))
            json = []
            for item in folder[0].children.all():
                file_dic = {}
                file_dic["name"] = item.name
                file_dic["id"] = item.id
                file_dic["url"] = item.pretty_logical_path
                file_dic["file_count"] = item.file_count
                file_dic["children_count"] = item.children_count
                # fix date
                date_to_str = str(item.modified_at)
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = True
                file_dic["parent_id"] = item.parent_id

                file_dic["extension"] = ""
                file_dic["size"] = ""
                json.append(file_dic)
            for item in folder[0].files.all():
                file_dic = {}
                file_dic["name"] = item.label
                file_dic["size"] = size(item.size, system=alternative)
                file_dic["url"] = "{0}://{1}{2}".format(request.scheme, request.get_host(), str(item.url))
                file_dic["id"] = item.id
                file_dic["extension"] = item.extension

                # fix date
                date_to_str = str(item.modified_at)
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = False
                file_dic["parent_id"] = item.folder_id

                file_dic["file_count"] = 0
                file_dic["children_count"] = 0

                json.append(file_dic)
            return Response(json)
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def GetRootFolders(request):
    if request.method == "POST":
        try:
            json = []
            for item in Folder.objects.all():
                if item.parent != None:
                    continue
                file_dic = {}
                file_dic["name"] = item.name
                file_dic["id"] = item.id
                file_dic["file_count"] = item.file_count
                file_dic["url"] = item.pretty_logical_path
                file_dic["children_count"] = item.children_count
                # fix date
                date_to_str = str(item.modified_at)
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = True
                file_dic["parent_id"] = item.parent_id

                file_dic["extension"] = ""
                file_dic["size"] = ""
                json.append(file_dic)
            return Response(json)
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})


@api_view(['POST', ])
def FindByRoot(request):
    if request.method == "POST":
        try:
            json = []
            for item in Folder.objects.filter(name__icontains=str(request.GET.get('name'))):
                #print(item.children_count)
                file_dic = {}
                file_dic["name"] = item.name
                file_dic["id"] = item.id
                file_dic["file_count"] = item.file_count
                file_dic["url"] = ""
                file_dic["children_count"] = item.children_count
                # fix date
                date_to_str = str(item.modified_at)
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = True
                file_dic["parent_id"] = item.parent_id

                file_dic["extension"] = ""
                file_dic["size"] = ""
                json.append(file_dic)

            for item in File.objects.filter(original_filename__icontains=str(request.GET.get('name'))).values().all():
                #print(item)
                file_dic = {}
                file_dic["name"] = item['original_filename']
                file_dic["id"] = item['id']
                file_dic["size"] = size(item['_file_size'], system=alternative)
                file_dic["url"] = "{0}://{1}/media/{2}".format(request.scheme, request.get_host(), str(item['file']))
                file_dic["extension"] = file_dic["name"].split(".")[-1]

                # fix date
                date_to_str = str(item['uploaded_at'])
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = False
                file_dic["parent_id"] = item['folder_id']

                file_dic["file_count"] = 0
                file_dic["children_count"] = 0
                json.append(file_dic)
            return Response(json)
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})



@api_view(['POST', ])
def FindByFolder(request):
    json = []
    def find_in_folder(id, name):
        for item in Folder.objects.filter(id=id):
            for files in item.files.filter(original_filename__icontains=name):
                file_dic = {}
                file_dic["name"] = files.label
                file_dic["size"] = size(files.size, system=alternative)
                file_dic["url"] = "{0}://{1}{2}".format(request.scheme, request.get_host(), str(files.url))
                file_dic["id"] = files.id
                file_dic["extension"] = files.extension

                # fix date
                date_to_str = str(files.modified_at)
                date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                last_ind = date_to_str.rfind(':')
                file_dic["date"] = date_to_str[:last_ind]

                file_dic["isFolder"] = False
                file_dic["parent_id"] = files.folder_id

                file_dic["file_count"] = 0
                file_dic["children_count"] = 0
                json.append(file_dic)

            sub_folders = item.children.all()
            for sub_folder in sub_folders:
                if name in sub_folder.name:
                    file_dic = {}
                    file_dic["name"] = sub_folder.name
                    file_dic["id"] = sub_folder.id
                    file_dic["file_count"] = sub_folder.file_count
                    file_dic["url"] = ""
                    file_dic["children_count"] = sub_folder.children_count
                    # fix date
                    date_to_str = str(sub_folder.modified_at)
                    date_to_str = date_to_str.replace('T', " ").replace("+00:00", "")
                    last_ind = date_to_str.rfind(':')
                    file_dic["date"] = date_to_str[:last_ind]

                    file_dic["isFolder"] = True
                    file_dic["parent_id"] = sub_folder.parent_id

                    file_dic["extension"] = ""
                    file_dic["size"] = ""
                    json.append(file_dic)
                find_in_folder(sub_folder.id, name)

    if request.method == "POST":
        try:
            find_in_folder(request.GET.get('id'), request.GET.get('name'))
            return Response(json)
        except KeyError:
            return Response({"result": False})
        except ValueError:
            return Response({"result": False})
        except:
            return Response({"result": False})



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def contac(request):
    return TemplateResponse(request, 'contact.html')


def ShowLicence(reqest):
    return HttpResponse(text_licence)
