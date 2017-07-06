def binary_search(list, item):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
mylist = ['anticlerical', 'antiwar', 'antler', 'apartheid', 'apartment', 'appalling', 'apparatus', 'application', 'approximant', 'approximate', 'arbitrary', 'arbitrate', 'area', 'brace', 'brainwash', 'brainwave',  'brand', 'breach', 'break', 'breath', 'brick', 'brickbat', 'bring', 'brinjal', 'brink', 'brocade', 'broomstick', 'bruschetta', 'brush', 'bubblejet', 'budgetary', 'building', 'bull', 'bulldog', 'bump', 'burdock','bureau', 'burn', 'bush', 'business', 'butch', 'butcher', 'buy', 'cab', 'cabal', 'cabaret', 'cabbage', 'cabbie', 'cabdriver', 'daffodil', 'daffy', 'daft', 'dag', 'dagger', 'dago', 'daguerreotype', 'dahlia', 'daikon', 'daily', 'e-bank', 'e-banking', 'e-blast', 'e-book', 'e-business', 'e-card', 'e-cash', 'e-cigarette', 'e-commerce', 'e-currency', 'e-enabled', 'e-entertainment', 'e-freight', 'e-fulfilment', 'e-goods', 'e-governance', 'e-invoice', 'e-journal', 'e-lance', 'e-learning', 'e-library', 'e-liquid', 'e-mall', 'e-marketing', 'e-marketplace', 'e-mentoring', 'e-money', 'e-news', 'e-prescribing', 'e-procurement', 'e-publishing', 'e-reader', 'e-recruitment', 'e-sports', 'e-tailer', 'e-tailing', 'e-ticket', 'e-ticketing', 'e-token', 'fab', 'fable', 'fabled', 'fabric', 'fabricate', 'fabulous', 'fabulously', 'faade', 'face', 'gaggle', 'gaiety', 'gaily', 'gain', 'hadj', 'hadn', 'hadron', 'hadst', 'haematite', 'haematology', 'idea', 'ideal', 'ideally', 'identical', 'identification', 'jab', 'jack', 'jacket', 'jagged', 'jaguar', 'jail', 'jam', 'jangle', 'janitor']

print(binary_search(mylist, 'application'))