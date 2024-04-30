import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter

doc = __revit__.ActiveUIDocument.Document

# Filtrando os elementos Generic Models
collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel)

# Lista para armazenar os parâmetros únicos encontrados
unique_parameters = set()

for element in collector:
    # Obtendo todas as propriedades (parâmetros) do elemento
    parameters = element.Parameters
    
    # Adicionando os nomes dos parâmetros à lista
    for param in parameters:
        unique_parameters.add(param.Definition.Name)

# Printando a lista de parâmetros únicos
print("Lista de parâmetros encontrados nos Generic Models:")
for param_name in unique_parameters:
    print(param_name)

# Parâmetro específico que queremos filtrar
parameter_name = "IfcPresentationLayer"

# Lista para armazenar os valores únicos do parâmetro específico
unique_values = set()

for element in collector:
    # Verificando se o parâmetro especificado está presente no elemento
    if element.LookupParameter(parameter_name):
        # Obtendo o valor do parâmetro
        parameter_value = element.LookupParameter(parameter_name).AsString()
        # Adicionando o valor à lista
        unique_values.add(parameter_value)

# Removendo valores vazios da lista
unique_values.discard(None)

# Printando os valores únicos do parâmetro específico
print(f"\nValores únicos do parâmetro '{parameter_name}':")
for index, value in enumerate(unique_values, 1):
    print(f"{index}. {value}")
    
# Parâmetro específico que queremos encontrar os valores
parameter_name = "Mobilia"

# Lista para armazenar os valores únicos do parâmetro específico
unique_values_mobilia = set()

for element in collector:
    # Verificando se o parâmetro especificado está presente no elemento
    if element.LookupParameter(parameter_name):
        # Obtendo o valor do parâmetro
        parameter_value_mobilia = element.LookupParameter(parameter_name).AsInteger()
        # Convertendo o valor para "Sim" ou "Não"
        if parameter_value_mobilia == 1:
            unique_values_mobilia.add("Sim")
        else:
            unique_values_mobilia.add("Não")

# Removendo valores vazios da lista
unique_values_mobilia.discard(None)

# Printando os valores únicos do parâmetro específico "Mobilia"
print(f"\nValores únicos do parâmetro '{parameter_name}':")
for index, value in enumerate(unique_values_mobilia, 1):
    print(f"{index}. {value}")
    
# Parâmetro específico que queremos contar
parameter_name = "Mobilia"

# Contador para armazenar a quantidade de elementos com o parâmetro "Mobilia"
count_mobilia_elements = 0

for element in collector:
    # Verificando se o parâmetro especificado está presente no elemento
    if element.LookupParameter(parameter_name):
        # Incrementando o contador
        count_mobilia_elements += 1

# Printando a quantidade de elementos com o parâmetro "Mobilia"
print(f"A quantidade de elementos com o parâmetro '{parameter_name}' é {count_mobilia_elements}")

# Valor específico do parâmetro "IfcPresentationLayer" que queremos filtrar
presentation_layer_value_to_filter = "ARQ - Eletrodoméstico & Mobiliário"

# Contador para armazenar a quantidade de elementos filtrados
count_elements_with_mobilia = 0

for element in collector:
    # Verificando se o parâmetro "IfcPresentationLayer" possui o valor desejado
    if element.LookupParameter("IfcPresentationLayer") and element.LookupParameter("IfcPresentationLayer").AsString() == presentation_layer_value_to_filter:
        # Incrementando o contador se o parâmetro "Mobilia" estiver presente no elemento
        if element.LookupParameter("Mobilia"):
            count_elements_with_mobilia += 1

# Printando a quantidade de elementos que possuem o parâmetro "Mobilia" dentro dos elementos filtrados
print(f"A quantidade de elementos com o valor '{presentation_layer_value_to_filter}' para 'IfcPresentationLayer' e com o parâmetro 'Mobilia' é {count_elements_with_mobilia}")

# Valor específico do parâmetro "IfcPresentationLayer" que queremos filtrar
presentation_layer_value_to_filter = "ARQ - Eletrodoméstico & Mobiliário"

# Iniciando uma transação
transaction = Transaction(doc, "Alterar propriedade 'Mobilia'")
transaction.Start()

try:
    # Loop através dos elementos filtrados
    for element in collector:
        # Verificando se o parâmetro "IfcPresentationLayer" possui o valor desejado
        if element.LookupParameter("IfcPresentationLayer") and element.LookupParameter("IfcPresentationLayer").AsString() == presentation_layer_value_to_filter:
            # Verificando se o parâmetro "Mobilia" está presente no elemento
            if element.LookupParameter("Mobilia"):
                # Definindo o parâmetro "Mobilia" como "Yes" (True)
                element.LookupParameter("Mobilia").Set(1)
    
    # Finalizando a transação
    transaction.Commit()
    print("A propriedade 'Mobilia' foi alterada para 'Yes' com sucesso.")
except Exception as e:
    # Caso ocorra um erro, cancelamos a transação
    transaction.RollBack()
    print(f"Erro ao definir 'Mobilia' como 'Yes': {str(e)}")
