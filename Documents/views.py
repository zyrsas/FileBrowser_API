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
from django.contrib.sites.models import Site


@api_view(['POST', ])
def SignUp(request):
    if request.method == "POST":
        try:
            """if User.objects.filter(name=request.GET.get('user')).count() == 0:
                if Department.objects.filter(id=request.GET.get('dep')).count() == 1:
                    if request.GET.get('regID') != None:
                        reg_ID = request.GET.get('regID')
                    else:
                        reg_ID = ""
                    new_user = User(name=request.GET.get('user'), password=request.GET.get('pass'), departmen_id=int(request.GET.get('dep')), regID=reg_ID)
                    new_user.save()

                    data_for_json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                             'name',
                                                                                             'departmen_id',
                                                                                             'departmen__name',
                                                                                             'access')
                    tmp = list(data_for_json)[0]

                    # id new user
                    user_id = tmp
                    user_id = user_id['id']

                    # add to database doc for user
                    userToDoc = User.objects.filter(id=user_id).values('departmen__documents__id')
                    print(list(userToDoc))
                    for i in list(userToDoc):
                        i = dict(i)
                        if ((i['departmen__documents__id'] != None) and (user_id != None)):
                            if not UserToDoc.objects.filter(user=user_id,
                                                            doc=i['departmen__documents__id']).exists():
                                user_to_doc = UserToDoc(user=user_id,
                                                        doc=i['departmen__documents__id'],
                                                        status=True)
                                user_to_doc.save()

                    return Response(tmp)

                else:
                    return Response({"SignUp": "Department not exist"})
            else:"""
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
                    print(list(reg_ID))
                    for i in reg_ID:
                        i.regID = request.GET.get('regID')
                        i.save()
                        print("Update")
                data_for_json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                         'name',
                                                                                         'access'
                                                                                         )
                tmp = list(data_for_json)[0]

                return Response(tmp)
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



def ShowLicence(reqest):
    return HttpResponse(text_licence)


@api_view(['POST', ])
def DeleteUserForTESTING(request):
    if request.method == "POST":
        try:
            User.objects.filter(id=request.GET.get('user_id')).delete()
            return Response({"result": True})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def GetFiles(request):
    if request.method == "POST":
        try:


            #for f in File.objects.all():
            #    print(f.path)
            #    print(f.url)
            #    print(f.folder)
            #    print()

            f = Folder.objects.filter(name="Бодя")
            for i in f:
                print(i.files)

            """for f in Folder.objects.all():
                print(f)
                print(f.file_count)
                print(f.parent)
                print(f.files.all())
                for i in f.files.all():
                    print(i.url)"""


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
            folder = []
            for f in Folder.objects.all():
                if f.parent == None:
                    folder.append(f.name)
                print("Folder name = ", f.name)
                print("File count = ", f.file_count)
                print("Children count = ", f.children_count)
                print("ID = ", f.id)
                print("ID_Parent", f.parent_id)
                print("Parent = ", f.parent)
                print("Created", f.created_at)
                print("Icons", f.icons)
                print("\n")


                """
                print("Folder name = ", f.name)
                print("File count = ", f.file_count)
                print("Children count = ", f.children_count)
                print("ID = ", f.id)
                print("ID_Parent", f.parent_id)
                print("Parent = ", f.parent)
                print("Created", f.created_at)
                print("Icons", f.icons)
                print("Files: ")
                """
            return Response({"folders": folder})
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
            folder = Folder.objects.filter(id=2)
            json = []
            for item in folder[0].children.all():
                print(item.name)
            for item in folder[0].files.all():
                file_dic = {}
                file_dic["name"] = item.label
                file_dic["size"] = item.size
                file_dic["url"] = "{0}://{1}{2}".format(request.scheme, request.get_host(), str(item.url))
                file_dic["id"] = item.id
                file_dic["extension"] = item.extension
                file_dic["date"] = item.modified_at
                json.append(file_dic)
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


