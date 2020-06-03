from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    description: str
    ingredients: dict
    instruction: list
    notes: str

    def print(self):
        recipe_dict = self.__dict__

        for key, value in recipe_dict.items():
            if key=='instruction':
                print(key)
                for i in range(len(value)):
                    print('\t',i+1,': ',value[i])
            elif key=='ingredients':
                print(key)
                for i in value:
                    if value[i][1] == 'items': print('\t',i,': ',value[i][0])
                    else: print('\t',i,': ',value[i][0],value[i][1])
            else: print(key,':',value)
