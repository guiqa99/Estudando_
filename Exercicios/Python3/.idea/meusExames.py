'''from tenant_connection.api_connection import *
from ..TOKEN.token import getJWT
from ..CONFIGS.configs import api_params
from ..USUARIO_HMC.autenticaUsuario import pacienteAutenticado
import requests
from flask import request'''

token = getJWT(api_params.get('exames')['scope'])['access_token']

headers = {
    "Content-Type": "application/json",
    "Authorization": token
}

def response():
    cpf = request.headers.get('cpf')

    user, code = pacienteAutenticado(cpf)
    
    if code == 200:        
        url = api_params.get('exames')['path'] + f"?codigoPaciente={user['codigo']}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            # exams_dict = {}
            # for exam in response.json():
            #     if 'dataRealizacao' in exam.keys():
            #         if exam['dataRealizacao'] not in exams_dict.keys():
            #             exams_dict[exam['dataRealizacao']] = [exams]
            #         else:
            #             exams_dict[exam['dataRealizacao']].append(exam)
                        
            exams_dict = {'REALIZADOS': [], 'AGENDADOS': []}
            for exam in response.json():
                if 'dataRealizacao' in exam.keys():
                    exams_dict['REALIZADOS'].append(exam)
                else:
                    exams_dict['AGENDADOS'].append(exam)            
            
            body = {
              "pageNavigation": {
                "background": "#F8F9FA",
                "color": "#000",
                "title": "Meus exames",
                "left": {
                  "actions": [
                    {
                      "order": "0",
                      "name": "back"
                    }
                  ]
                }
              },
              "pageHeader": {
                "template": "A",
                "background": "#F8F9FA",
                "logo": None,
                "color": "#FFF",
                "item": {
                  "publishLevel": 1,
                  "details": [
                    {
                      "order": 0,
                      "value": ""
                    }
                  ],
                  "actionDefault": 0,
                  "actions": [
            
                  ]
                }
              },
              "pageContent": {
                "hasGroupBy": True,
                "background": "#F8F9FA",
                "totalPages": 1,
                "groupList": [
                  {
                    "template": "B",
                    "title": category,
                    "background": "#F8F9FA",
                    "startsCollapsed": False,
                    "itemsList": [
                      {
                        "id": f"{idx}",
                        "color": "#333",
                        "background": "#FFFFFF",
                        "publishLevel": 1,
                        "permissionLevel": 1,
                        "actionDefault": 0,
                        "details": [
                          {
                            "order": 0,
                            "value": f"""<span><b>{exam['nome']}</b></span><br><div style= 'font-size: 13px'>{exam['nomeMedico']}</div><strong><div style= 'font-size: 10px; color: #12ed78'>LAUDADO</div></strong>"""
                          } if str(exam['status']) == '1' else {
                            "order": 0,
                            "value": f"""<span><b>{exam['nome']}</b></span><br><div style= 'font-size: 13px'>{exam['nomeMedico']}</div><div style= 'font-size: 10px; color: #000fff'>NÃO LAUDADO</div>"""
                          }
                        ],
                        "actions": [
                          {
                            "order": 0,
                            "title": "Laudo",
                            "publishLevel": 1,
                            "permissionLevel": 1,
                            "name": "open-pdf",
                            "path": "MEUHOSPITAL",
                            "parameters": [
                              {
                                "title": "querystring",
                                "value": f"CMS/detalheExame/response?sequenciaExame={exam['sequencia']}&sequenciaPrescricao={exam['sequenciaPrescricao']}"
                              }
                            ]
                          } if str(exam['status']) == '1' else {}
                        ]
                      } for idx, exam in enumerate(exams)
                    ]
                  } for category, exams in exams_dict.items()
                ]
              }
            }
            
            return body, 200

        return {
            "pageNavigation": {
                "background": "#F8F9FA",
                "color": "#000",
                "title": "Meus exames",
                "left": {
                    "actions": [
                        {
                            "order": "0",
                            "name": "back"
                        }
                    ]
                }
            },
        
        "message": "Nenhum exame encontrado!"}, 404

    return {"message": "Você não possui cadastro no hospital!"}, 400
    
def next_pages():
    return {'message': ['MEUHOSPITAL']}, 200
    
