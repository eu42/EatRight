from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.model.ateFood import AteFood
from api.model.ateIngredient import AteIngredient
from api.model.diet import Diet
from api.model.food import Food
from api.model.inclusion import Inclusion
from api.model.ingredient import Ingredient
from api.model.restaurant import Restaurant


@api_view(['GET'])
def createMocks(req):

    Ingredient.objects.all().delete()
    User.objects.all().delete()
    Restaurant.objects.all().delete()
    Food.objects.all().delete()
    Diet.objects.all().delete()
    AteFood.objects.all().delete()
    AteIngredient.objects.all().delete()

    RiceFlour      = Ingredient(name='Rice flour'     ,measureValue=125 ,measureUnit='ml'     ,defaultValue=83  ,defaultUnit='g'   ,energy=305 ,protein=5   ,carb=67  ,sugar=1   ,fibre=0.3  ,fat=0    ,saturatedFat=8    ,cholesterol=0.3  ,calcium=0    ,iron=63.0 ,sodium=29.0 ,potassium=82.0 ,magnesium=0.1   ,phosphorus=0.02  ,thiamin=3.2  ,riboflavin=3    ,niacin=0    ,folate=1   )
    SoyFlour       = Ingredient(name='Soy flour'      ,measureValue=125 ,measureUnit='ml'     ,defaultValue=53  ,defaultUnit='g'   ,energy=174 ,protein=25  ,carb=20  ,sugar=11  ,fibre=9.2  ,fat=1    ,saturatedFat=0.1  ,cholesterol=0    ,calcium=127  ,iron=4.9  ,sodium=11.0 ,potassium=1259 ,magnesium=153   ,phosphorus=356   ,thiamin=0.4  ,riboflavin=0.13 ,niacin=7.4  ,folate=161 )
    WheatBran      = Ingredient(name='Wheat bran'     ,measureValue=125 ,measureUnit='ml'     ,defaultValue=4   ,defaultUnit='g'   ,energy=8   ,protein=1   ,carb=2   ,sugar=0   ,fibre=1.6  ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=3    ,iron=0.4  ,sodium=0    ,potassium=43   ,magnesium=22    ,phosphorus=37    ,thiamin=0    ,riboflavin=0.02 ,niacin=0.7  ,folate=3   )
    Bread          = Ingredient(name='Bread'          ,measureValue=125 ,measureUnit='ml'     ,defaultValue=64  ,defaultUnit='g'   ,energy=170 ,protein=6   ,carb=35  ,sugar=1   ,fibre=4.7  ,fat=2    ,saturatedFat=0.3  ,cholesterol=0    ,calcium=10   ,iron=2    ,sodium=340  ,potassium=109  ,magnesium=44.0  ,phosphorus=115   ,thiamin=0.2  ,riboflavin=0.05 ,niacin=3.4  ,folate=22  )
    Biscuit        = Ingredient(name='Biscuit'        ,measureValue=1   ,measureUnit='count'  ,defaultValue=51  ,defaultUnit='g'   ,energy=186 ,protein=3   ,carb=25  ,sugar=2   ,fibre=0.7  ,fat=8    ,saturatedFat=1.3  ,cholesterol=1    ,calcium=25   ,iron=1.7  ,sodium=537  ,potassium=114  ,magnesium=9.0   ,phosphorus=219   ,thiamin=0.2  ,riboflavin=0.15 ,niacin=2.4  ,folate=58  )
    GranolaBar     = Ingredient(name='Granola bar'    ,measureValue=1   ,measureUnit='count'  ,defaultValue=25  ,defaultUnit='g'   ,energy=118 ,protein=3   ,carb=16  ,sugar=0   ,fibre=1.3  ,fat=5    ,saturatedFat=0.6  ,cholesterol=0    ,calcium=15   ,iron=0.7  ,sodium=74   ,potassium=84   ,magnesium=24.0  ,phosphorus=69.0  ,thiamin=0.1  ,riboflavin=0.03 ,niacin=1.1  ,folate=6   )
    ChocolateChip  = Ingredient(name='Chocolate chip' ,measureValue=1   ,measureUnit='count'  ,defaultValue=20  ,defaultUnit='g'   ,energy=98  ,protein=1   ,carb=13  ,sugar=7   ,fibre=0.6  ,fat=5    ,saturatedFat=1.5  ,cholesterol=0    ,calcium=7    ,iron=0.7  ,sodium=59   ,potassium=30   ,magnesium=10    ,phosphorus=23    ,thiamin=0    ,riboflavin=0.05 ,niacin=0.7  ,folate=20  )
    BeanSprouts    = Ingredient(name='Bean sprouts'   ,measureValue=125 ,measureUnit='g'      ,defaultValue=66  ,defaultUnit='ml'  ,energy=125 ,protein=137 ,carb=3   ,sugar=7   ,fibre=0    ,fat=1.2  ,saturatedFat=0    ,cholesterol=9    ,calcium=1.2  ,iron=6    ,sodium=143  ,potassium=22   ,magnesium=52    ,phosphorus=1     ,thiamin=12   ,riboflavin=0    ,niacin=46   ,folate=10  )
    Cabbage        = Ingredient(name='Cabbage'        ,measureValue=125 ,measureUnit='ml'     ,defaultValue=37  ,defaultUnit='g'   ,energy=9   ,protein=1   ,carb=2   ,sugar=1   ,fibre=0.7  ,fat=0    ,saturatedFat=17   ,cholesterol=0.2  ,calcium=7    ,iron=91   ,sodium=6    ,potassium=9    ,magnesium=3     ,phosphorus=33    ,thiamin=0    ,riboflavin=16   ,niacin=12   ,folate=0   )
    Carrot         = Ingredient(name='Carrot'         ,measureValue=1   ,measureUnit='count'  ,defaultValue=61  ,defaultUnit='g'   ,energy=25  ,protein=1   ,carb=6   ,sugar=3   ,fibre=1.5  ,fat=0    ,saturatedFat=20   ,cholesterol=0.2  ,calcium=42   ,iron=195  ,sodium=7    ,potassium=21   ,magnesium=367   ,phosphorus=3522  ,thiamin=1    ,riboflavin=12   ,niacin=4    ,folate=0   )
    Cucumber       = Ingredient(name='Cucumber'       ,measureValue=4   ,measureUnit='slice'  ,defaultValue=28  ,defaultUnit='g'   ,energy=3   ,protein=0   ,carb=1   ,sugar=0   ,fibre=0.2  ,fat=0    ,saturatedFat=4    ,cholesterol=0.1  ,calcium=1    ,iron=3    ,sodium=8    ,potassium=3    ,magnesium=6     ,phosphorus=1     ,thiamin=9    ,riboflavin=0    ,niacin=4    ,folate=10  )
    Eggplant       = Ingredient(name='Eggplant'       ,measureValue=125 ,measureUnit='ml'     ,defaultValue=52  ,defaultUnit='g'   ,energy=18  ,protein=0   ,carb=5   ,sugar=2   ,fibre=1.3  ,fat=0    ,saturatedFat=3    ,cholesterol=0.1  ,calcium=1    ,iron=64   ,sodium=6    ,potassium=8    ,magnesium=1     ,phosphorus=12    ,thiamin=0    ,riboflavin=7    ,niacin=1    ,folate=0   )
    Lettuce        = Ingredient(name='Lettuce'        ,measureValue=250 ,measureUnit='ml'     ,defaultValue=58  ,defaultUnit='g'   ,energy=8   ,protein=1   ,carb=1   ,sugar=1   ,fibre=0.6  ,fat=0    ,saturatedFat=20   ,cholesterol=0.7  ,calcium=3    ,iron=138  ,sodium=8    ,potassium=19   ,magnesium=96    ,phosphorus=1155  ,thiamin=0    ,riboflavin=42   ,niacin=2    ,folate=0   )
    Mushrooms      = Ingredient(name='Mushrooms'      ,measureValue=3   ,measureUnit='medium' ,defaultValue=54  ,defaultUnit='g'   ,energy=12  ,protein=2   ,carb=2   ,sugar=1   ,fibre=0.6  ,fat=0    ,saturatedFat=2    ,cholesterol=0.3  ,calcium=2    ,iron=170  ,sodium=5    ,potassium=46   ,magnesium=0     ,phosphorus=0     ,thiamin=0    ,riboflavin=9    ,niacin=1    ,folate=0.2 )
    Onion          = Ingredient(name='Onion'          ,measureValue=1   ,measureUnit='medium' ,defaultValue=15  ,defaultUnit='g'   ,energy=5   ,protein=0   ,carb=1   ,sugar=0   ,fibre=0.4  ,fat=0    ,saturatedFat=11   ,cholesterol=0.2  ,calcium=2    ,iron=41   ,sodium=3    ,potassium=6    ,magnesium=8     ,phosphorus=90    ,thiamin=0    ,riboflavin=10   ,niacin=3    ,folate=0   )
    Potato         = Ingredient(name='Potato'         ,measureValue=1   ,measureUnit='count'  ,defaultValue=156 ,defaultUnit='g'   ,energy=145 ,protein=3   ,carb=34  ,sugar=3   ,fibre=3.4  ,fat=0    ,saturatedFat=8    ,cholesterol=0.5  ,calcium=8    ,iron=610  ,sodium=39   ,potassium=78   ,magnesium=0     ,phosphorus=0     ,thiamin=0    ,riboflavin=14   ,niacin=20   ,folate=0   )
    Radishes       = Ingredient(name='Radishes'       ,measureValue=3   ,measureUnit='medium' ,defaultValue=14  ,defaultUnit='g'   ,energy=2   ,protein=0   ,carb=0   ,sugar=0   ,fibre=0.2  ,fat=0    ,saturatedFat=3    ,cholesterol=0    ,calcium=5    ,iron=31   ,sodium=1    ,potassium=3    ,magnesium=0     ,phosphorus=1     ,thiamin=0    ,riboflavin=3    ,niacin=2    ,folate=0   )
    Tomatoe        = Ingredient(name='Tomatoe'        ,measureValue=1   ,measureUnit='count'  ,defaultValue=123 ,defaultUnit='g'   ,energy=22  ,protein=1   ,carb=5   ,sugar=3   ,fibre=1.5  ,fat=0    ,saturatedFat=12   ,cholesterol=0.3  ,calcium=6    ,iron=292  ,sodium=14   ,potassium=30   ,magnesium=52    ,phosphorus=552   ,thiamin=3165 ,riboflavin=18   ,niacin=16   ,folate=0   )
    Apple          = Ingredient(name='Apple'          ,measureValue=1   ,measureUnit='count'  ,defaultValue=138 ,defaultUnit='g'   ,energy=72  ,protein=0   ,carb=19  ,sugar=14  ,fibre=2.6  ,fat=0    ,saturatedFat=8    ,cholesterol=0.2  ,calcium=1    ,iron=148  ,sodium=7    ,potassium=15   ,magnesium=4     ,phosphorus=37    ,thiamin=0    ,riboflavin=4    ,niacin=6    ,folate=0   )
    Banana         = Ingredient(name='Banana'         ,measureValue=1   ,measureUnit='count'  ,defaultValue=118 ,defaultUnit='g'   ,energy=105 ,protein=1   ,carb=27  ,sugar=14  ,fibre=2.1  ,fat=0    ,saturatedFat=6    ,cholesterol=0.3  ,calcium=1    ,iron=422  ,sodium=32   ,potassium=26   ,magnesium=4     ,phosphorus=31    ,thiamin=0    ,riboflavin=24   ,niacin=10   ,folate=0   )
    Figs           = Ingredient(name='Figs'           ,measureValue=1   ,measureUnit='count'  ,defaultValue=50  ,defaultUnit='g'   ,energy=37  ,protein=0   ,carb=10  ,sugar=8   ,fibre=1.5  ,fat=0    ,saturatedFat=18   ,cholesterol=0.2  ,calcium=1    ,iron=116  ,sodium=9    ,potassium=7    ,magnesium=4     ,phosphorus=43    ,thiamin=0    ,riboflavin=3    ,niacin=1    ,folate=0   )
    Grapes         = Ingredient(name='Grapes'         ,measureValue=20  ,measureUnit='count'  ,defaultValue=100 ,defaultUnit='g'   ,energy=69  ,protein=1   ,carb=18  ,sugar=15  ,fibre=1.2  ,fat=0    ,saturatedFat=10   ,cholesterol=0.4  ,calcium=2    ,iron=191  ,sodium=7    ,potassium=20   ,magnesium=3     ,phosphorus=39    ,thiamin=0    ,riboflavin=2    ,niacin=11   ,folate=0   )
    Mango          = Ingredient(name='Mango'          ,measureValue=1   ,measureUnit='count'  ,defaultValue=104 ,defaultUnit='g'   ,energy=67  ,protein=1   ,carb=18  ,sugar=15  ,fibre=1.9  ,fat=0    ,saturatedFat=10   ,cholesterol=0.1  ,calcium=2    ,iron=161  ,sodium=9    ,potassium=11   ,magnesium=39    ,phosphorus=461   ,thiamin=0    ,riboflavin=14   ,niacin=29   ,folate=0   )
    Orange         = Ingredient(name='Orange'         ,measureValue=1   ,measureUnit='count'  ,defaultValue=131 ,defaultUnit='g'   ,energy=62  ,protein=1   ,carb=15  ,sugar=12  ,fibre=2.3  ,fat=0    ,saturatedFat=52   ,cholesterol=0.1  ,calcium=0    ,iron=237  ,sodium=13   ,potassium=18   ,magnesium=8     ,phosphorus=93    ,thiamin=0    ,riboflavin=39   ,niacin=70   ,folate=0   )
    Peach          = Ingredient(name='Peach'          ,measureValue=1   ,measureUnit='count'  ,defaultValue=98  ,defaultUnit='g'   ,energy=38  ,protein=1   ,carb=9   ,sugar=8   ,fibre=1.9  ,fat=0    ,saturatedFat=6    ,cholesterol=0.2  ,calcium=0    ,iron=186  ,sodium=9    ,potassium=20   ,magnesium=16    ,phosphorus=159   ,thiamin=0    ,riboflavin=3    ,niacin=6    ,folate=0   )
    Pear           = Ingredient(name='Pear'           ,measureValue=1   ,measureUnit='count'  ,defaultValue=166 ,defaultUnit='g'   ,energy=96  ,protein=1   ,carb=26  ,sugar=16  ,fibre=5.0  ,fat=0    ,saturatedFat=15   ,cholesterol=0.3  ,calcium=2    ,iron=198  ,sodium=12   ,potassium=18   ,magnesium=2     ,phosphorus=22    ,thiamin=0    ,riboflavin=12   ,niacin=7    ,folate=0   )
    Raspberries    = Ingredient(name='Raspberries'    ,measureValue=125 ,measureUnit='ml'     ,defaultValue=65  ,defaultUnit='g'   ,energy=34  ,protein=1   ,carb=8   ,sugar=3   ,fibre=4.2  ,fat=0    ,saturatedFat=16   ,cholesterol=0.4  ,calcium=1    ,iron=98   ,sodium=14   ,potassium=19   ,magnesium=1     ,phosphorus=8     ,thiamin=0    ,riboflavin=14   ,niacin=17   ,folate=0   )
    Strawberries   = Ingredient(name='Strawberries'   ,measureValue=7   ,measureUnit='count'  ,defaultValue=84  ,defaultUnit='g'   ,energy=27  ,protein=1   ,carb=6   ,sugar=4   ,fibre=1.9  ,fat=0    ,saturatedFat=13   ,cholesterol=0.4  ,calcium=1    ,iron=129  ,sodium=11   ,potassium=20   ,magnesium=1     ,phosphorus=6     ,thiamin=0    ,riboflavin=20   ,niacin=49   ,folate=0   )
    Buttermilk     = Ingredient(name='Buttermilk'     ,measureValue=250 ,measureUnit='ml'     ,defaultValue=259 ,defaultUnit='g'   ,energy=104 ,protein=9   ,carb=12  ,sugar=12  ,fibre=2    ,fat=1.4  ,saturatedFat=10   ,cholesterol=300  ,calcium=0.1  ,iron=272  ,sodium=391  ,potassium=28   ,magnesium=230   ,phosphorus=18    ,thiamin=0.2  ,riboflavin=13   ,niacin=0.57 ,folate=0.40)
    Milk           = Ingredient(name='Milk'           ,measureValue=250 ,measureUnit='ml'     ,defaultValue=259 ,defaultUnit='g'   ,energy=88  ,protein=9   ,carb=13  ,sugar=13  ,fibre=0    ,fat=0.2  ,saturatedFat=5    ,cholesterol=324  ,calcium=0.1  ,iron=109  ,sodium=404  ,potassium=28   ,magnesium=261   ,phosphorus=158   ,thiamin=2.7  ,riboflavin=13   ,niacin=1.37 ,folate=0.47)
    Yogourt        = Ingredient(name='Yogourt'        ,measureValue=200 ,measureUnit='ml'     ,defaultValue=207 ,defaultUnit='g'   ,energy=145 ,protein=5   ,carb=24  ,sugar=24  ,fibre=3    ,fat=2.1  ,saturatedFat=12   ,cholesterol=191  ,calcium=0.2  ,iron=81   ,sodium=257  ,potassium=23   ,magnesium=157   ,phosphorus=0     ,thiamin=0.2  ,riboflavin=25   ,niacin=0.58 ,folate=0.23)
    Cheddar        = Ingredient(name='Cheddar'        ,measureValue=50  ,measureUnit='g'      ,defaultValue=50  ,defaultUnit='g'   ,energy=202 ,protein=12  ,carb=1   ,sugar=0   ,fibre=17   ,fat=10.5 ,saturatedFat=53   ,cholesterol=361  ,calcium=0.3  ,iron=311  ,sodium=49   ,potassium=14   ,magnesium=256   ,phosphorus=133   ,thiamin=0.1  ,riboflavin=9    ,niacin=0.42 ,folate=0.19)
    CottageCheese  = Ingredient(name='Cottage cheese' ,measureValue=125 ,measureUnit='ml'     ,defaultValue=119 ,defaultUnit='g'   ,energy=86  ,protein=1   ,carb=5   ,sugar=3   ,fibre=3    ,fat=1    ,saturatedFat=0.8  ,cholesterol=573  ,calcium=0.2  ,iron=500  ,sodium=103  ,potassium=6    ,magnesium=160   ,phosphorus=13    ,thiamin=0    ,riboflavin=14   ,niacin=0.75 ,folate=0.20)
    CreamCheese    = Ingredient(name='Cream cheese'   ,measureValue=30  ,measureUnit='ml'     ,defaultValue=29  ,defaultUnit='g'   ,energy=103 ,protein=2   ,carb=1   ,sugar=0   ,fibre=10   ,fat=6.5  ,saturatedFat=32   ,cholesterol=24   ,calcium=0.4  ,iron=87   ,sodium=35   ,potassium=2    ,magnesium=31    ,phosphorus=108   ,thiamin=0    ,riboflavin=4    ,niacin=0.12 ,folate=0.3 )
    FetaCheese     = Ingredient(name='Feta cheese'    ,measureValue=50  ,measureUnit='g'      ,defaultValue=50  ,defaultUnit='g'   ,energy=132 ,protein=7   ,carb=2   ,sugar=2   ,fibre=11   ,fat=7.7  ,saturatedFat=46   ,cholesterol=247  ,calcium=0.3  ,iron=558  ,sodium=31   ,potassium=10   ,magnesium=169   ,phosphorus=63    ,thiamin=0.2  ,riboflavin=16   ,niacin=0.87 ,folate=0.44)
    Mozzarella     = Ingredient(name='Mozzarella'     ,measureValue=50  ,measureUnit='g'      ,defaultValue=50  ,defaultUnit='g'   ,energy=141 ,protein=10  ,carb=1   ,sugar=1   ,fibre=11   ,fat=6.8  ,saturatedFat=39   ,cholesterol=269  ,calcium=0.1  ,iron=187  ,sodium=34   ,potassium=10   ,magnesium=186   ,phosphorus=90    ,thiamin=0.1  ,riboflavin=4    ,niacin=0.33 ,folate=0.13)
    SourCream      = Ingredient(name='Sour cream'     ,measureValue=15  ,measureUnit='g'      ,defaultValue=15  ,defaultUnit='g'   ,energy=22  ,protein=0   ,carb=1   ,sugar=0   ,fibre=2    ,fat=1.3  ,saturatedFat=6    ,cholesterol=16   ,calcium=0    ,iron=6    ,sodium=19   ,potassium=1    ,magnesium=14    ,phosphorus=17    ,thiamin=0.1  ,riboflavin=2    ,niacin=0.04 ,folate=0.02)
    Egg            = Ingredient(name='Egg'            ,measureValue=1   ,measureUnit='count'  ,defaultValue=33  ,defaultUnit='g'   ,energy=16  ,protein=3   ,carb=0   ,sugar=0   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=3    ,iron=0    ,sodium=106  ,potassium=39   ,magnesium=4     ,phosphorus=0     ,thiamin=0    ,riboflavin=0    ,niacin=0.01 ,folate=0   )
    Beef           = Ingredient(name='Beef'           ,measureValue=75  ,measureUnit='g'      ,defaultValue=75  ,defaultUnit='g'   ,energy=200 ,protein=26  ,carb=0   ,sugar=10  ,fibre=4.0  ,fat=5.0  ,saturatedFat=0.4  ,cholesterol=71   ,calcium=2.5  ,iron=46   ,sodium=202  ,potassium=18   ,magnesium=142   ,phosphorus=0     ,thiamin=0.5  ,riboflavin=2.38 ,niacin=4    ,folate=0.1 )
    Veal           = Ingredient(name='Veal'           ,measureValue=75  ,measureUnit='g'      ,defaultValue=75  ,defaultUnit='g'   ,energy=173 ,protein=23  ,carb=0   ,sugar=9   ,fibre=3.2  ,fat=3.3  ,saturatedFat=0.6  ,cholesterol=86   ,calcium=0.9  ,iron=65   ,sodium=244  ,potassium=20   ,magnesium=179   ,phosphorus=0     ,thiamin=1.1  ,riboflavin=1.18 ,niacin=11   ,folate=0.3 )
    Pork           = Ingredient(name='Pork'           ,measureValue=75  ,measureUnit='g'      ,defaultValue=75  ,defaultUnit='g'   ,energy=274 ,protein=21  ,carb=0   ,sugar=20  ,fibre=7.9  ,fat=8.9  ,saturatedFat=2.6  ,cholesterol=85   ,calcium=0.9  ,iron=100  ,sodium=251  ,potassium=18   ,magnesium=147   ,phosphorus=2     ,thiamin=0.8  ,riboflavin=0.83 ,niacin=2    ,folate=0   )
    Lamb           = Ingredient(name='Lamb'           ,measureValue=75  ,measureUnit='g'      ,defaultValue=75  ,defaultUnit='g'   ,energy=182 ,protein=21  ,carb=0   ,sugar=10  ,fibre=4.2  ,fat=4.3  ,saturatedFat=0.7  ,cholesterol=80   ,calcium=1.6  ,iron=54   ,sodium=193  ,potassium=17   ,magnesium=125   ,phosphorus=0     ,thiamin=0.2  ,riboflavin=1.71 ,niacin=13   ,folate=0.1 )
    Chicken        = Ingredient(name='Chicken'        ,measureValue=75  ,measureUnit='g'      ,defaultValue=75  ,defaultUnit='g'   ,energy=142 ,protein=19  ,carb=0   ,sugar=7   ,fibre=1.8  ,fat=2.6  ,saturatedFat=1.4  ,cholesterol=63   ,calcium=0.4  ,iron=45   ,sodium=241  ,potassium=20   ,magnesium=0     ,phosphorus=20    ,thiamin=0.2  ,riboflavin=0.24 ,niacin=3    ,folate=0.2 )
    Falafel        = Ingredient(name='Falafel'        ,measureValue=1   ,measureUnit='ball'   ,defaultValue=17  ,defaultUnit='g'   ,energy=57  ,protein=2   ,carb=5   ,sugar=0   ,fibre=1.3  ,fat=3    ,saturatedFat=0.4  ,cholesterol=1.7  ,calcium=0.7  ,iron=9    ,sodium=0.6  ,potassium=50   ,magnesium=99    ,phosphorus=14    ,thiamin=33   ,riboflavin=18   ,niacin=0    ,folate=0   )
    Beans          = Ingredient(name='Beans'          ,measureValue=175 ,measureUnit='ml'     ,defaultValue=187 ,defaultUnit='g'   ,energy=283 ,protein=10  ,carb=40  ,sugar=0   ,fibre=10.3 ,fat=10   ,saturatedFat=3.6  ,cholesterol=4.0  ,calcium=1.4  ,iron=114  ,sodium=3.7  ,potassium=790  ,magnesium=670   ,phosphorus=80    ,thiamin=204  ,riboflavin=90   ,niacin=0    ,folate=0   )
    Lentils        = Ingredient(name='Lentils'        ,measureValue=175 ,measureUnit='ml'     ,defaultValue=179 ,defaultUnit='g'   ,energy=190 ,protein=14  ,carb=32  ,sugar=0   ,fibre=5.9  ,fat=1    ,saturatedFat=0.2  ,cholesterol=0.3  ,calcium=0.6  ,iron=22   ,sodium=4.1  ,potassium=4    ,magnesium=317   ,phosphorus=39    ,thiamin=161  ,riboflavin=112  ,niacin=0    ,folate=0   )
    Peas           = Ingredient(name='Peas'           ,measureValue=175 ,measureUnit='ml'     ,defaultValue=145 ,defaultUnit='g'   ,energy=171 ,protein=12  ,carb=31  ,sugar=4   ,fibre=4.2  ,fat=1    ,saturatedFat=0.1  ,cholesterol=0.1  ,calcium=0.2  ,iron=20   ,sodium=1.9  ,potassium=3    ,magnesium=525   ,phosphorus=52    ,thiamin=144  ,riboflavin=94   ,niacin=0    ,folate=0   )
    Soybeans       = Ingredient(name='Soybeans'       ,measureValue=175 ,measureUnit='ml'     ,defaultValue=127 ,defaultUnit='g'   ,energy=220 ,protein=21  ,carb=13  ,sugar=4   ,fibre=8.0  ,fat=11   ,saturatedFat=1.7  ,cholesterol=2.5  ,calcium=6.4  ,iron=130  ,sodium=6.5  ,potassium=1    ,magnesium=655   ,phosphorus=109   ,thiamin=312  ,riboflavin=69   ,niacin=0    ,folate=0   )
    PeanutButter   = Ingredient(name='Peanut butter'  ,measureValue=30  ,measureUnit='ml'     ,defaultValue=32  ,defaultUnit='g'   ,energy=191 ,protein=8   ,carb=7   ,sugar=3   ,fibre=2.6  ,fat=16   ,saturatedFat=2.6  ,cholesterol=8.0  ,calcium=4.8  ,iron=15   ,sodium=0.6  ,potassium=158  ,magnesium=242   ,phosphorus=52    ,thiamin=103  ,riboflavin=30   ,niacin=0    ,folate=2.0 )
    Almonds        = Ingredient(name='Almonds'        ,measureValue=60  ,measureUnit='ml'     ,defaultValue=36  ,defaultUnit='g'   ,energy=208 ,protein=8   ,carb=7   ,sugar=2   ,fibre=4.2  ,fat=18   ,saturatedFat=1.4  ,cholesterol=11.6 ,calcium=4.4  ,iron=89   ,sodium=1.5  ,potassium=0    ,magnesium=262   ,phosphorus=99    ,thiamin=171  ,riboflavin=10   ,niacin=0    ,folate=9.3 )
    Hazelnuts      = Ingredient(name='Hazelnuts'      ,measureValue=60  ,measureUnit='ml'     ,defaultValue=34  ,defaultUnit='g'   ,energy=215 ,protein=5   ,carb=6   ,sugar=1   ,fibre=3.3  ,fat=21   ,saturatedFat=1.5  ,cholesterol=15.6 ,calcium=2.7  ,iron=39   ,sodium=1.6  ,potassium=0    ,magnesium=233   ,phosphorus=56    ,thiamin=99   ,riboflavin=39   ,niacin=0    ,folate=5.2 )
    Walnuts        = Ingredient(name='Walnuts'        ,measureValue=60  ,measureUnit='ml'     ,defaultValue=25  ,defaultUnit='g'   ,energy=166 ,protein=4   ,carb=3   ,sugar=1   ,fibre=1.7  ,fat=17   ,saturatedFat=1.6  ,cholesterol=2.3  ,calcium=12.0 ,iron=25   ,sodium=0.7  ,potassium=1    ,magnesium=112   ,phosphorus=40    ,thiamin=88   ,riboflavin=25   ,niacin=0    ,folate=0.2 )
    BrownSugar     = Ingredient(name='Brown sugar'    ,measureValue=5   ,measureUnit='ml'     ,defaultValue=5   ,defaultUnit='g'   ,energy=18  ,protein=0   ,carb=5   ,sugar=4   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=4    ,iron=0.1  ,sodium=2    ,potassium=16   ,magnesium=1     ,phosphorus=1     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=0   )
    WhiteSugar     = Ingredient(name='White sugar'    ,measureValue=5   ,measureUnit='ml'     ,defaultValue=4   ,defaultUnit='g'   ,energy=16  ,protein=0   ,carb=4   ,sugar=4   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=0    ,iron=0    ,sodium=0    ,potassium=0    ,magnesium=0     ,phosphorus=0     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=0   )
    BrownSugar     = Ingredient(name='Brown sugar'    ,measureValue=5   ,measureUnit='ml'     ,defaultValue=5   ,defaultUnit='g'   ,energy=18  ,protein=0   ,carb=5   ,sugar=4   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=4    ,iron=0.1  ,sodium=2    ,potassium=16   ,magnesium=1     ,phosphorus=1     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=0   )
    Cola           = Ingredient(name='Cola'           ,measureValue=250 ,measureUnit='ml'     ,defaultValue=262 ,defaultUnit='g'   ,energy=110 ,protein=0   ,carb=28  ,sugar=24  ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=8    ,iron=0.1  ,sodium=10   ,potassium=3    ,magnesium=3     ,phosphorus=34    ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=26  )
    Coffee         = Ingredient(name='Coffee'         ,measureValue=250 ,measureUnit='ml'     ,defaultValue=250 ,defaultUnit='g'   ,energy=3   ,protein=0   ,carb=0   ,sugar=0   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=5    ,iron=0    ,sodium=5    ,potassium=123  ,magnesium=8     ,phosphorus=8     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=100 )
    CoffeeLatte    = Ingredient(name='Coffee latte'   ,measureValue=250 ,measureUnit='ml'     ,defaultValue=256 ,defaultUnit='g'   ,energy=101 ,protein=5   ,carb=7   ,sugar=9   ,fibre=0    ,fat=6    ,saturatedFat=3.5  ,cholesterol=16   ,calcium=188  ,iron=0.2  ,sodium=79   ,potassium=340  ,magnesium=89    ,phosphorus=156   ,thiamin=46   ,riboflavin=0    ,niacin=0    ,folate=93  )
    Tea            = Ingredient(name='Tea'            ,measureValue=250 ,measureUnit='ml'     ,defaultValue=250 ,defaultUnit='g'   ,energy=3   ,protein=0   ,carb=1   ,sugar=0   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=0    ,iron=0.1  ,sodium=8    ,potassium=93   ,magnesium=8     ,phosphorus=3     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=0   )
    Ketchup        = Ingredient(name='Ketchup'        ,measureValue=15  ,measureUnit='ml'     ,defaultValue=15  ,defaultUnit='g'   ,energy=15  ,protein=0   ,carb=4   ,sugar=3   ,fibre=0    ,fat=0    ,saturatedFat=0    ,cholesterol=0    ,calcium=0    ,iron=3    ,sodium=0.1  ,potassium=169  ,magnesium=57    ,phosphorus=3     ,thiamin=5    ,riboflavin=7    ,niacin=0    ,folate=2586)
    Mustard        = Ingredient(name='Mustard'        ,measureValue=15  ,measureUnit='ml'     ,defaultValue=16  ,defaultUnit='g'   ,energy=11  ,protein=1   ,carb=1   ,sugar=0   ,fibre=1    ,fat=0    ,saturatedFat=0.4  ,cholesterol=0.2  ,calcium=0    ,iron=9    ,sodium=0.2  ,potassium=180  ,magnesium=22    ,phosphorus=8     ,thiamin=17   ,riboflavin=1    ,niacin=0    ,folate=0   )
    Mayonnaise     = Ingredient(name='Mayonnaise'     ,measureValue=15  ,measureUnit='ml'     ,defaultValue=14  ,defaultUnit='g'   ,energy=100 ,protein=0   ,carb=1   ,sugar=11  ,fibre=1.7  ,fat=2.7  ,saturatedFat=6.0  ,cholesterol=0    ,calcium=5    ,iron=3    ,sodium=0.1  ,potassium=79   ,magnesium=5     ,phosphorus=0     ,thiamin=4    ,riboflavin=11   ,niacin=0    ,folate=0   )
    Ranch          = Ingredient(name='Ranch'          ,measureValue=15  ,measureUnit='ml'     ,defaultValue=15  ,defaultUnit='g'   ,energy=71  ,protein=0   ,carb=1   ,sugar=8   ,fibre=1.2  ,fat=1.7  ,saturatedFat=4.2  ,cholesterol=0    ,calcium=5    ,iron=5    ,sodium=0.1  ,potassium=120  ,magnesium=9     ,phosphorus=1     ,thiamin=24   ,riboflavin=1    ,niacin=0    ,folate=0   )
    GreenPepper    = Ingredient(name='Green Pepper'   ,measureValue=0.5 ,measureUnit='count'  ,defaultValue=82  ,defaultUnit='g'   ,energy=16  ,protein=1   ,carb=4   ,sugar=2   ,fibre=1.2  ,fat=0    ,saturatedFat=8    ,cholesterol=0.3  ,calcium=2    ,iron=144  ,sodium=8    ,potassium=16   ,magnesium=15    ,phosphorus=171   ,thiamin=0    ,riboflavin=9    ,niacin=0    ,folate=66  )
    RedPepper      = Ingredient(name='Red Pepper'     ,measureValue=0.5 ,measureUnit='count'  ,defaultValue=60  ,defaultUnit='g'   ,energy=15  ,protein=1   ,carb=4   ,sugar=2   ,fibre=0.8  ,fat=0    ,saturatedFat=4    ,cholesterol=0.3  ,calcium=1    ,iron=126  ,sodium=7    ,potassium=15   ,magnesium=93    ,phosphorus=966   ,thiamin=183  ,riboflavin=11   ,niacin=0    ,folate=113 )
    BlackPepper    = Ingredient(name='Black Pepper'   ,measureValue=125 ,measureUnit='ml'     ,defaultValue=74  ,defaultUnit='g'   ,energy=99  ,protein=1   ,carb=5   ,sugar=3   ,fibre=1.3  ,fat=9    ,saturatedFat=5    ,cholesterol=0.4  ,calcium=16   ,iron=144  ,sodium=9    ,potassium=17   ,magnesium=98    ,phosphorus=1169  ,thiamin=361  ,riboflavin=1    ,niacin=0    ,folate=121 )
    Butter         = Ingredient(name='Butter'         ,measureValue=5   ,measureUnit='ml'     ,defaultValue=5   ,defaultUnit='g'   ,energy=34  ,protein=0   ,carb=0   ,sugar=4   ,fibre=2.5  ,fat=1.0  ,saturatedFat=0.1  ,cholesterol=0.2  ,calcium=10   ,iron=1    ,sodium=0    ,potassium=28   ,magnesium=1     ,phosphorus=0     ,thiamin=1    ,riboflavin=33   ,niacin=0    ,folate=0   )
    Margarine      = Ingredient(name='Margarine'      ,measureValue=5   ,measureUnit='ml'     ,defaultValue=5   ,defaultUnit='g'   ,energy=34  ,protein=0   ,carb=0   ,sugar=4   ,fibre=0.6  ,fat=1.7  ,saturatedFat=1.3  ,cholesterol=0    ,calcium=1    ,iron=0    ,sodium=52   ,potassium=2    ,magnesium=0     ,phosphorus=1     ,thiamin=48   ,riboflavin=0.6  ,niacin=0    ,folate=0.2 )
    SunflowerOil   = Ingredient(name='Sunflower Oil'  ,measureValue=15  ,measureUnit='ml'     ,defaultValue=14  ,defaultUnit='g'   ,energy=122 ,protein=0   ,carb=0   ,sugar=14  ,fibre=1.4  ,fat=2.7  ,saturatedFat=9.1  ,cholesterol=0.1  ,calcium=0    ,iron=0    ,sodium=0    ,potassium=0    ,magnesium=0     ,phosphorus=0     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=5.7 )
    Sesame         = Ingredient(name='Sesame'         ,measureValue=15  ,measureUnit='ml'     ,defaultValue=14  ,defaultUnit='g'   ,energy=122 ,protein=0   ,carb=0   ,sugar=14  ,fibre=2.0  ,fat=5.5  ,saturatedFat=5.7  ,cholesterol=0    ,calcium=0    ,iron=0    ,sodium=0    ,potassium=0    ,magnesium=0     ,phosphorus=0     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=0.2 )
    Salt           = Ingredient(name='Salt'           ,measureValue=15  ,measureUnit='ml'     ,defaultValue=14  ,defaultUnit='g'   ,energy=122 ,protein=0   ,carb=0   ,sugar=14  ,fibre=2.0  ,fat=5.5  ,saturatedFat=5.7  ,cholesterol=0    ,calcium=0    ,iron=0    ,sodium=0    ,potassium=0    ,magnesium=0     ,phosphorus=0     ,thiamin=0    ,riboflavin=0    ,niacin=0    ,folate=0.2 )
    ChickenBreast  = Ingredient(name='Chicken breast' ,measureValue=75  ,measureUnit='g'      ,defaultValue=75  ,defaultUnit='g'   ,energy=142 ,protein=19  ,carb=0   ,sugar=7   ,fibre=1.8  ,fat=2.6  ,saturatedFat=1.4  ,cholesterol=63   ,calcium=0.4  ,iron=45   ,sodium=241  ,potassium=20   ,magnesium=0     ,phosphorus=20    ,thiamin=0.2  ,riboflavin=0.24 ,niacin=0    ,folate=3   )

    for ingredient in [RiceFlour, SoyFlour, WheatBran, Bread, Biscuit, GranolaBar, ChocolateChip, BeanSprouts, Cabbage, Carrot, Cucumber, Eggplant, Lettuce, Mushrooms, Onion, Potato, Radishes, Tomatoe, Apple, Banana, Figs, Grapes, Mango, Orange, Peach, Pear, Raspberries, Strawberries, Buttermilk, Milk, Yogourt, Cheddar, CottageCheese, CreamCheese, FetaCheese, Mozzarella, SourCream, Egg, Beef, Veal, Pork, Lamb, Chicken, Falafel, Beans, Lentils, Peas, Soybeans, PeanutButter, Almonds, Hazelnuts, Walnuts, BrownSugar, WhiteSugar, BrownSugar, Cola, Coffee, CoffeeLatte, Tea, Ketchup, Mustard, Mayonnaise, Ranch, GreenPepper, RedPepper, BlackPepper, Butter, Margarine, SunflowerOil, Sesame, Salt, ChickenBreast]:
        ingredient.save()

    Kagan           = User(first_name='Kagan', last_name='Sari',       username='kagannsari@gmail.com',   email='kagannsari@gmail.com')
    Erkam           = User(first_name='Erkam', last_name='Uyanik',     username='erkam@hotmail.com',      email='erkam@hotmail.com')
    Arda            = User(first_name='Arda',  last_name='Yoruk',      username='arda@hotmail.com',       email='arda@hotmail.com')
    Murat           = User(first_name='Murat', last_name='Aclan',      username='murat@hotmail.com',      email='murat@hotmail.com')
    Yigit           = User(first_name='Yigit', last_name='Ozgumus',    username='yigit@hotmail.com',      email='yigit@hotmail.com')
    Gozde           = User(first_name='Gozde', last_name='Berk',       username='gozde@hotmail.com',      email='gozde@hotmail.com')
    Enes            = User(first_name='Enes',  last_name='Ozipek',     username='enes@hotmail.com',       email='enes@hotmail.com')
    AhmetMcDonalds  = User(first_name='Ahmet', last_name='McDonalds',  username='info@mcdonalds.com',     email='info@mcdonalds.com')
    AhmetBurgerKing = User(first_name='Ahmet', last_name='BurgerKing', username='info@burgerking.com',    email='info@burgerking.com')
    AhmetMutfak     = User(first_name='Ahmet', last_name='Mutfak',     username='info@mutfak.com',        email='info@mutfak.com')
    NecmiAbi        = User(first_name='Necmi', last_name='Abi',        username='info@kuzeykantin.com',   email='info@kuzeykantin.com')
    OmerAybak       = User(first_name='Omer' , last_name='Aybak',      username='cigkofte02@hotmail.com', email='cigkofte02@hotmail.com')

    for user in [Kagan, Erkam, Arda, Murat, Yigit, Gozde, Enes, AhmetMcDonalds, AhmetBurgerKing, AhmetMutfak]:
        user.set_password('123456')
        user.save()

    Mcdonalds   = Restaurant(user=AhmetMcDonalds,  name='McDonalds Bebek',       description='McDonalds gibisi yok',          photo='http://www.commondreams.org/sites/default/files/styles/cd_large/public/views-article/mcdonald_0.jpg?itok=IWMtMwHS')
    BurgerKing  = Restaurant(user=AhmetBurgerKing, name='Burger King Hisarustu', description='Ates seni cagriyo',             photo='http://images.techtimes.com/data/images/full/142491/burger-king.jpg')
    Mutfak      = Restaurant(user=AhmetMutfak,     name='Mutfak',                description=None,                            photo='https://lalgeziyor.files.wordpress.com/2016/07/ekran-resmi-2016-07-18-18-29-36.png')
    KuzeyKantin = Restaurant(user=NecmiAbi,        name='Kuzey Kantin',          description=None,                            photo='http://www.otk.boun.edu.tr/lisans/sites/default/files/14249692_611736205671349_6342629255368353570_o.jpg')
    Adiyaman    = Restaurant(user=OmerAybak,       name='Adiyaman',              description='Meshur adiyaman cig koctecisi', photo='https://lh3.googleusercontent.com/7qDc8280Y4obPJfxmYAAI3EdWiQ_spw1Ywhuar8_RsGdUyRIVQCWPP6Ys8mxemsTIzT2jX4=s630-fcrop64=1,00000000fd5afdfa')

    for restaurant in [Mcdonalds, BurgerKing, Mutfak]:
        restaurant.save()

    BigKingMenu = Food(name='Big King Menu', restaurant=BurgerKing, photo='https://www.burgerking.com.tr/cmsfiles/products/big-king-menu-1.png?v=96')
    BigKingMenu.save()
    BigKingMenu.inclusion_set.add(Inclusion(ingredient=Beef, value=150, unit='g'), bulk=False)
    BigKingMenu.inclusion_set.add(Inclusion(ingredient=Bread, value=300, unit='g'), bulk=False)
    BigKingMenu.inclusion_set.add(Inclusion(ingredient=Potato, value=200, unit='g'), bulk=False)
    BigKingMenu.inclusion_set.add(Inclusion(ingredient=Cola, value=300, unit='g'), bulk=False)
    BigKingMenu.inclusion_set.add(Inclusion(ingredient=Onion, value=50, unit='g'), bulk=False)
    BigKingMenu.inclusion_set.add(Inclusion(ingredient=Lettuce, value=30, unit='g'), bulk=False)

    WhopperMenu = Food(name='Whopper Menu', user=AhmetBurgerKing, restaurant=BurgerKing, photo='https://www.burgerking.com.tr/cmsfiles/products/double-whopper-menu.png?v=96')
    WhopperMenu.save()
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Beef, value=120, unit='g'), bulk=False)
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Bread, value=300, unit='g'), bulk=False)
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Potato, value=300, unit='g'), bulk=False)
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Cola, value=400, unit='g'), bulk=False)
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Onion, value=30, unit='g'), bulk=False)
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Ketchup, value=20, unit='g'), bulk=False)
    WhopperMenu.inclusion_set.add(Inclusion(ingredient=Mayonnaise, value=20, unit='g'), bulk=False)

    Manti = Food(name='Manti', user=AhmetMutfak, restaurant=Mutfak, photo='http://img.nefisyemektarifleri.net/2008/07/manti-tarifi1-500x333.jpg')
    Manti.save()
    Manti.inclusion_set.add(Inclusion(ingredient=RiceFlour, value=120, unit='g'), bulk=False)
    Manti.inclusion_set.add(Inclusion(ingredient=Beef, value=30, unit='g'), bulk=False)
    Manti.inclusion_set.add(Inclusion(ingredient=Onion, value=30, unit='g'), bulk=False)
    Manti.inclusion_set.add(Inclusion(ingredient=RedPepper, value=10, unit='g'), bulk=False)
    Manti.inclusion_set.add(Inclusion(ingredient=Yogourt, value=10, unit='g'), bulk=False)


    Vegan = Diet(name="Vegan", minEnergy=0, maxEnergy=9999, minProteinVal=0, maxProteinVal=9999, minCarbVal=0, maxCarbVal=9999, minFatVal=0, maxFatVal=9999, minProteinRate=0, maxProteinRate=1, minCarbRate=0, maxCarbRate=1, minFatRate=0, maxFatRate=1)
    Vegan.save()

    Vegetarian = Diet(name="Vegetarian", minEnergy=0, maxEnergy=9999, minProteinVal=0, maxProteinVal=9999, minCarbVal=0, maxCarbVal=9999, minFatVal=0, maxFatVal=9999, minProteinRate=0, maxProteinRate=1, minCarbRate=0, maxCarbRate=1, minFatRate=0, maxFatRate=1)
    Vegetarian.save()

    Gozde.diet_set = [Vegan, Vegetarian]
    Gozde.save()

    return Response()
