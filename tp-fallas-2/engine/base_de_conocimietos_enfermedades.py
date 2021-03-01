SINTOMAS = ['fiebre_mayor_37', 'dolor_garganta', 'cansancio', 'anosmia',
            'ageusia', 'tos_seca', 'cefalea', 'secrecion_nasal',
            'grupo_riesgo', 'contacto_estrecho', 'cant_contagios_zona']

GRIPE_COMUN = 'Gripe Comun'
COVID = 'COVID19'
NEUMONIA = 'Neumonia'
RESFRIO = 'Resfrio'
DIAGNOSTICOS = [GRIPE_COMUN,  COVID, NEUMONIA, RESFRIO]

r1 = {'diagnostico': GRIPE_COMUN,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "NORMAL",
                   'dif_respirar': "NADA",
                   'cansancio': "NORMAL",
                   'anosmia': "NADA",
                   'ageusia': "NADA",
                   'tos_seca': "PREEXISTENTE",
                   'cefalea': True,
                   'secrecion_nasal': False,
                   'grupo_riesgo': True,
                   'contacto_estrecho': "NO",
                   'cant_contagios_zona': "BAJO"}
      }
r2 = {'diagnostico': COVID,
      'sintomas': {'fiebre_mayor_37': False,
                   'dolor_garganta': "NADA",
                   'dif_respirar': "NADA",
                   'cansancio': "NADA",
                   'anosmia': "AGUDA",
                   'ageusia': "AGUDA",
                   'tos_seca': "NADA",
                   'cefalea': True,
                   'secrecion_nasal': False,
                   'grupo_riesgo': False,
                   'contacto_estrecho': "CASUAL",
                   'cant_contagios_zona': "ALTO"}
      }
r3 = {'diagnostico': COVID,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "INTENSO",
                   'dif_respirar': "PREEXISTENTE",
                   'cansancio': "INTENSO",
                   'anosmia': "PREEXISTENTE",
                   'ageusia': "PREEXISTENTE",
                   'tos_seca': "AGUDA",
                   'cefalea': False,
                   'secrecion_nasal': False,
                   'grupo_riesgo': False,
                   'contacto_estrecho': "PERMANENTE",
                   'cant_contagios_zona': "ALTO"}
      }
r4 = {'diagnostico': GRIPE_COMUN,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "INTENSO",
                   'dif_respirar': "NADA",
                   'cansancio': "INTENSO",
                   'anosmia': "NADA",
                   'ageusia': "NADA",
                   'tos_seca': "AGUDA",
                   'cefalea': True,
                   'secrecion_nasal': True,
                   'grupo_riesgo': True,
                   'contacto_estrecho': "NO",
                   'cant_contagios_zona': "SINCASOS"}
      }

r5 = {'diagnostico': NEUMONIA,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "NADA",
                   'dif_respirar': "AGUDA",
                   'cansancio': "NORMAL",
                   'anosmia': "NADA",
                   'ageusia': "NADA",
                   'tos_seca': "AGUDA",
                   'cefalea': False,
                   'secrecion_nasal': False,
                   'grupo_riesgo': False,
                   'contacto_estrecho': "NO",
                   'cant_contagios_zona': "ALTO"}
      }

r6 = {'diagnostico': RESFRIO,
      'sintomas': {'fiebre_mayor_37': False,
                   'dolor_garganta': "INTENSO",
                   'dif_respirar': "AGUDA",
                   'cansancio': "NADA",
                   'anosmia': "NADA",
                   'ageusia': "NADA",
                   'tos_seca': "NADA",
                   'cefalea': False,
                   'secrecion_nasal': True,
                   'grupo_riesgo': True,
                   'contacto_estrecho': "CASUAL",
                   'cant_contagios_zona': "BAJO"}
      }

r7 = {'diagnostico': COVID,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "NORMAL",
                   'dif_respirar': "NADA",
                   'cansancio': "NORMAL",
                   'anosmia': "AGUDA",
                   'ageusia': "NADA",
                   'tos_seca': "PREEXISTENTE",
                   'cefalea': True,
                   'secrecion_nasal': True,
                   'grupo_riesgo': False,
                   'contacto_estrecho': "CASUAL",
                   'cant_contagios_zona': "ALTO"}
      }

r8 = {'diagnostico': COVID,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "NADA",
                   'dif_respirar': "AGUDA",
                   'cansancio': "INTENSO",
                   'anosmia': "NADA",
                   'ageusia': "NADA",
                   'tos_seca': "AGUDA",
                   'cefalea': False,
                   'secrecion_nasal': True,
                   'grupo_riesgo': True,
                   'contacto_estrecho': "PERMANENTE",
                   'cant_contagios_zona': "ALTO"}
      }

r9 = {'diagnostico': COVID,
      'sintomas': {'fiebre_mayor_37': True,
                   'dolor_garganta': "INTENSO",
                   'dif_respirar': "AGUDA",
                   'cansancio': "INTENSO",
                   'anosmia': "PREEXISTENTE",
                   'ageusia': "AGUDA",
                   'tos_seca': "AGUDA",
                   'cefalea': True,
                   'secrecion_nasal': False,
                   'grupo_riesgo': False,
                   'contacto_estrecho': "PERMANENTE",
                   'cant_contagios_zona': "BAJO"}
      }

r10 = {'diagnostico': COVID,
       'sintomas': {'fiebre_mayor_37': False,
                    'dolor_garganta': "INTENSO",
                    'dif_respirar': "NADA",
                    'cansancio': "NADA",
                    'anosmia': "NADA",
                    'ageusia': "NADA",
                    'tos_seca': "AGUDA",
                    'cefalea': True,
                    'secrecion_nasal': True,
                    'grupo_riesgo': True,
                    'contacto_estrecho': "NO",
                    'cant_contagios_zona': "ALTO"}
      }

class Paciente():
    def __init__(self):
        self.sintomas = {}

    def agregar_sintoma(self, key, value):
        if key in SINTOMAS:
            self.sintomas[key] = value


class ConocimientoMedico():

    def __init__(self):
        self.reglas = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
        self.sintomas = SINTOMAS
        self.diagnosticos = DIAGNOSTICOS

    def get_diagnose_for_rule(self, ruleidx):
        return self.reglas[ruleidx]['diagnostico']
