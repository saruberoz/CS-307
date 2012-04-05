#########################################
#  USERS                                #
#########################################
if db(db.auth_user.id > 0).count() == 0:
    db.auth_user.insert(
            first_name='Kevin',
            last_name='Schenk',
            username="schenkkp",
            email='schenkkp@gmail.com',
            password=db.auth_user.password.validate('cs307')[0]
        )
    db.auth_user.insert(
            first_name='Jaye',
            last_name='Franklin',
            username="jfranklin",
            email='jfrankl@purdue.edu',
            password=db.auth_user.password.validate('cs307')[0]
        )
    db.auth_user.insert(
            first_name='Kevin',
            last_name='Houtz',
            username="khoutz",
            email='khoutz@purdue.edu',
            password=db.auth_user.password.validate('cs307')[0]
        )
    db.auth_user.insert(
            first_name='Wilson',
            last_name='Sumanang',
            username="wsumanang",
            email='wilson.sumanang@gmail.com',
            password=db.auth_user.password.validate('cs307')[0]
        )
    db.auth_user.insert(
            first_name='Frank',
            last_name='Buibish',
            username="fbuibish",
            email='fbuibish@gmail.com',
            password=db.auth_user.password.validate('cs307')[0]
        )
    db.auth_user.insert(
            first_name='Test',
            last_name='User',
            username="test",
            email='schenkk@purdue.edu',
            password=db.auth_user.password.validate('cs307')[0]
        )

#########################################
#  COLLECTIONS                          #
#########################################
if db(db.collection.id > 0).count() == 0:
    db.collection.insert(
            user= db.auth_user(username='schenkkp'),
            name= "My Test Collection"
        )
    db.collection.insert(
            user= db.auth_user(username='schenkkp'),
            name= "My Thanksgiving Dinner"
        )
    db.collection.insert(
            user= db.auth_user(username='schenkkp'),
            name= "Conflicting Ingredients"
        )
    db.collection.insert(
            user= db.auth_user(username='khoutz'),
            name= "Conflicting Ingredients"
        )

#########################################
#  CATEGORIES                           #
#########################################
if db(db.category.id > 0).count() == 0:
    db.category.insert(
            name='Appetizers & Snacks',
            url_str='appetizers'
        )
    db.category.insert(
            name='Breads',
            url_str='breads'
        )
    db.category.insert(
            name='Breakfast',
            url_str='breakfast'
        )
    db.category.insert(
            name='Desserts',
            url_str='desserts'
        )
    db.category.insert(
            name='Drinks',
            url_str='drinks'
        )
    db.category.insert(
            name='Main Dishes',
            url_str='main-dishes'
        )
    db.category.insert(
            name='Salads',
            url_str='salads'
        )
    db.category.insert(
            name='Soups',
            url_str='soups'
        )

#########################################
#  IngredientName                       #
#########################################
if db(db.ingredientName.id > 0).count() == 0:
    db.ingredientName.insert(
            name= "milk"
        )
    db.ingredientName.insert(
            name= "water"
        )
    db.ingredientName.insert(
            name= "bacon"
        )
    db.ingredientName.insert(
            name= "large onions, peeled and chopped"
        )
    db.ingredientName.insert(
            name= "minced garlic"
        )
    db.ingredientName.insert(
            name= "toasted coriander seeds, ground"
        )
    db.ingredientName.insert(
            name= "ground cinnamon"
        )
    db.ingredientName.insert(
            name= "paprika"
        )
    db.ingredientName.insert(
            name= "cayenne pepper"
        )
    db.ingredientName.insert(
            name= "ground dried Poblano chili peppers"
        )
    db.ingredientName.insert(
            name= "Italian plum tomatoes, with juice"
        )
    db.ingredientName.insert(
            name= "beer"
        )
    db.ingredientName.insert(
            name= "lean ground beef"
        )
    db.ingredientName.insert(
            name= "salt"
        )
    db.ingredientName.insert(
            name= "Hellmann\'s or Best Foods Real Mayonnaise"
        )
    db.ingredientName.insert(
            name= "grated Parmesan cheese"
        )
    db.ingredientName.insert(
            name= "boneless, skinless chicken breast halves"
        )
    db.ingredientName.insert(
            name= "Italian seasoned dry bread crumbs"
        )
    db.ingredientName.insert(
            name= "cream cheese, softened"
        )
    db.ingredientName.insert(
            name= "chili without beans"
        )
    db.ingredientName.insert(
            name= "green onions, thinly sliced"
        )
    db.ingredientName.insert(
            name= "diced green chiles, drained"
        )
    db.ingredientName.insert(
            name= "shredded Cheddar cheese"
        )
    

#########################################
#  RECIPES                              #
#########################################
if db(db.recipe.id > 0).count() == 0:
    db.recipe.insert(
            name='Arcadian Eight Bean Chili',
            cook_time='30',
            prep_time='15',
            ingredients='- 1/4 lb  each of the following dried beans:  kidney, white, pink, black, red, pinto, cranberry, and navy\n'
'- 1 lb bacon\n'
'- 5 large onions, peeled and chopped\n'
'- 2/3 C minced garlic\n'
'- 1/4 C toasted coriander seeds, ground\n'
'- 1/4 C ground cinnamon\n'
'- 1/4 C paprika\n'
'- 1/4 C cayenne pepper, or to taste for the timid of tongue\n'
'- 1/2 C ground dried Poblano chili peppers\n'
'- 108 oz (#10 can) Italian plum tomatoes, with juice\n'
'- 12 oz beer\n'
'- 5 lb lean ground beef\n'
'- 1 dash salt to taste\n',
            directions='+ In a large pot, soak the beans together overnight in water to cover.\n'
'+ Drain and add fresh water to cover.  Cook at a simmer for  1 1/2 hours or until beans are just tender.\n'
'+ While the beans are simmering, heat a large skillet.  Mince the bacon and cook it until it begins to crisp.  Add the onions and garlic and cook over medium heat for 5 minutes.  Add all the spices and the ground Poblanos and cook another 5 minutes.  Add the tomatoes with their juice and the beer.  Simmer for half an hour.\n'
'+ In another pan, cook the beef until the pink color disappears.  Drain and add it to tomato mixture.\n'
'+ When the beans are fully cooked, drain them, reserving the liquid, and add the beans to the meat/tomato mixture.  Salt to taste and let the mixture simmer for about 1 hour.  If it is too dry, add some of the bean liquid.\n',
            user= db.auth_user(username='jfranklin'),
            category= db.category(name='Soups'),
            private=False
        )
    db.recipe.insert(
            name='Parmesan Crusted Chicken',
            cook_time='30',
            prep_time='15',
            ingredients='- 1/2 cup Hellmann\'s or Best Foods Real Mayonnaise\n'
'- 1/4 cup grated Parmesan cheese\n'
'- 4 (5 ounce) boneless, skinless chicken breast halves\n'
'- 4 teaspoons Italian seasoned dry bread crumbs\n',
            directions='+ Preheat oven to 425 degrees F.\n'
'+ Combine Hellmann\'s or Best Foods Real Mayonnaise with cheese in medium bowl.\n'
'+ Arrange chicken on baking sheet. Evenly top with mayonnaise mixture, then sprinkle with bread crumbs.\n'
'+ Bake 20 minutes or until chicken is thoroughly cooked.\n',
            user= db.auth_user(username='schenkkp'),
            category= db.category(name='Main Dishes'),
            private=False
        )
    db.recipe.insert(
            name='Double Chili Cheese Dip',
            cook_time='20',
            prep_time='5',
            ingredients='- 1 (8 ounce) package cream cheese, softened\n'
'- 1 (15 ounce) can chili without beans\n'
'- 4 green onions, thinly sliced\n'
'- 1/4 cup diced green chiles, drained\n'
'- 1 cup shredded Cheddar cheese\n',
            directions='+ Preheat oven to 350 degrees F (175 degrees C). Grease a 9-inch pie plate.\n'
'+ Spread cream cheese into the prepared pie plate. Top the cream cheese with chili, onions, chilies, and cheese.\n'
'+ Bake at 350 degrees F (175 degrees C) for 15 to 20 minutes.\n',
            user= db.auth_user(username='test'),
            category= db.category(name='Appetizers & Snacks'),
            private=False
        )
    db.recipe.insert(
            name='Chocolate Mint Cookies',
            cook_time='',
            prep_time='',
            ingredients='- 3/4 cup butter\n'
'- 1 1/2 cups packed brown sugar\n'
'- 2 tablespoons water\n'
'- 2 cups semisweet chocolate chips\n'
'- 2 eggs\n'
'- 2 1/2 cups all-purpose flour\n'
'- 1 1/4 teaspoons baking soda\n'
'- 1/2 teaspoon salt\n'
'- 36 chocolate mint wafer candies\n',
            directions='+ In a large pan over low heat, cook butter, sugar and water until butter is melted. Add chocolate chips and stir until partially melted. Remove from heat and continue to stir until chocolate is completely melted. Pour into a large bowl and let stand 10 minutes to cool off slightly.\n'
'+ At high speed, beat in eggs, one at a time into chocolate mixture. Reduce speed to low and add dry ingredients, beating until blended. Chill dough about 1 hour.\n'
'+ Preheat oven to 350 degrees F (175 degrees C).\n'
'+ Roll dough into balls and place on ungreased cookie sheet about 2 inches apart. Bake 8-10 minutes. While cookies are baking unwrap mints and divide each in half. When cookies are brought out of the oven, put 1/2 mint on top of each cookie. Let the mint sit for up to 5 minutes until melted, then spread the mint on top of the cookie. Eat and enjoy!\n',
            user= db.auth_user(username='schenkkp'),
            category= db.category(name='Desserts'),
            private=False
        )
    db.recipe.insert(
            name='Chocolate Chocolate Chip Cookies',
            cook_time='10',
            prep_time='15',
            ingredients='- 1 cup butter, softened\n'
'- 1 1/2 cups white sugar\n'
'- 2 eggs\n'
'- 2 teaspoons vanilla extract\n'
'- 2 cups all-purpose flour\n'
'- 2/3 cup cocoa powder\n'
'- 3/4 teaspoon baking soda\n'
'- 1/4 teaspoon salt\n'
'- 2 cups semisweet chocolate chips\n'
'- 1/2 cup chopped walnuts (optional)\n',
            directions='+ Preheat oven to 350 degrees F (175 degrees C).\n'
'+ In large bowl, beat butter, sugar, eggs, and vanilla until light and fluffy. Combine the flour, cocoa, baking soda, and salt; stir into the butter mixture until well blended. Mix in the chocolate chips and walnuts. Drop by rounded teaspoonfuls onto ungreased cookie sheets.\n'
'+ Bake for 8 to 10 minutes in the preheated oven, or just until set. Cool slightly on the cookie sheets before transferring to wire racks to cool completely.\n',
            user= db.auth_user(username='schenkkp'),
            category= db.category(name='Desserts'),
            private=False
        )
    db.recipe.insert(
            name='Too Much Chocolate Cake',
            cook_time='',
            prep_time='',
            ingredients='- 1 (18.25 ounce) package devil\'s food cake mix\n'
'- 1 (5.9 ounce) package instant chocolate pudding mix\n'
'- 1 cup sour cream\n'
'- 1 cup vegetable oil\n'
'- 4 eggs\n'
'- 1/2 cup warm water\n'
'- 2 cups semisweet chocolate chips\n',
            directions='+ Preheat oven to 350 degrees F (175 degrees C).\n'
'+ In a large bowl, mix together the cake and pudding mixes, sour cream, oil, beaten eggs and water. Stir in the chocolate chips and pour batter into a well greased 12 cup bundt pan.\n'
'+ Bake for 50 to 55 minutes, or until top is springy to the touch and a wooden toothpick inserted comes out clean. Cool cake thoroughly in pan at least an hour and a half before inverting onto a plate If desired, dust the cake with powdered sugar.\n',
            user= db.auth_user(username='schenkkp'),
            category= db.category(name='Desserts'),
            private=False
        )
    db.recipe.insert(
            name='Chicken Pot Pie',
            cook_time='',
            prep_time='',
            ingredients='- 1 pound skinless, boneless chicken breast halves - cubed\n'
'- 1 cup sliced carrots\n'
'- 1 cup frozen green peas\n'
'- 1/2 cup sliced celery\n'
'- 1/3 cup butter\n'
'- 1/3 cup chopped onion\n'
'- 1/3 cup all-purpose flour\n'
'- 1/2 teaspoon salt\n'
'- 1/4 teaspoon black pepper\n'
'- 1/4 teaspoon celery seed\n'
'- 1 3/4 cups chicken broth\n'
'- 2/3 cup milk\n',
            directions='+ Preheat oven to 425 degrees F (220 degrees C.)\n'
'+ In a saucepan, combine chicken, carrots, peas, and celery. Add water to cover and boil for 15 minutes. Remove from heat, drain and set aside.\n'
'+ In the saucepan over medium heat, cook onions in butter until soft and translucent. Stir in flour, salt, pepper, and celery seed. Slowly stir in chicken broth and milk. Simmer over medium-low heat until thick. Remove from heat and set aside.\n'
'+ Place the chicken mixture in bottom pie crust. Pour hot liquid mixture over. Cover with top crust, seal edges, and cut away excess dough. Make several small slits in the top to allow steam to escape.\n'
'+ Bake in the preheated oven for 30 to 35 minutes, or until pastry is golden brown and filling is bubbly. Cool for 10 minutes before serving.\n',
            user= db.auth_user(username='schenkkp'),
            category= db.category(name='Main Dishes'),
            private=False
        )
    
#########################################
#  Ingredient                           #
#########################################
if db(db.ingredient.id > 0).count() == 0:
    db.ingredient.insert(
            quantity='1',
            unit='lb',
            ingredient=db.ingredientName(name='bacon'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='5',
            unit='',
            ingredient=db.ingredientName(name='large onions, peeled and chopped'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.666666666666',
            unit='cup',
            ingredient=db.ingredientName(name='minced garlic'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.25',
            unit='cup',
            ingredient=db.ingredientName(name='toasted coriander seeds, ground'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.25',
            unit='cup',
            ingredient=db.ingredientName(name='ground cinnamon'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.25',
            unit='cup',
            ingredient=db.ingredientName(name='paprika'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.25',
            unit='cup',
            ingredient=db.ingredientName(name='cayenne pepper'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.5',
            unit='cup',
            ingredient=db.ingredientName(name='ground dried Poblano chili peppers'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='108',
            unit='oz',
            ingredient=db.ingredientName(name='Italian plum tomatoes, with juice'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='12',
            unit='oz',
            ingredient=db.ingredientName(name='beer'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='5',
            unit='lb',
            ingredient=db.ingredientName(name='lean ground beef'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='1',
            unit='dash',
            ingredient=db.ingredientName(name='salt'),
            recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.ingredient.insert(
            quantity='.5',
            unit='cup',
            ingredient=db.ingredientName(name='Hellmann\'s or Best Foods Real Mayonnaise'),
            recipe=db.recipe(name='Parmesan Crusted Chicken')
    )
    db.ingredient.insert(
            quantity='.25',
            unit='cup',
            ingredient=db.ingredientName(name='grated Parmesan cheese'),
            recipe=db.recipe(name='Parmesan Crusted Chicken')
    )
    db.ingredient.insert(
            quantity='4',
            unit='',
            ingredient=db.ingredientName(name='boneless, skinless chicken breast halves'),
            recipe=db.recipe(name='Parmesan Crusted Chicken')
    )
    db.ingredient.insert(
            quantity='4',
            unit='tsp',
            ingredient=db.ingredientName(name='Italian seasoned dry bread crumbs'),
            recipe=db.recipe(name='Parmesan Crusted Chicken')
    )
    db.ingredient.insert(
            quantity='8',
            unit='oz',
            ingredient=db.ingredientName(name='cream cheese, softened'),
            recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.ingredient.insert(
            quantity='15',
            unit='oz',
            ingredient=db.ingredientName(name='chili without beans'),
            recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.ingredient.insert(
            quantity='4',
            unit='',
            ingredient=db.ingredientName(name='green onions, thinly sliced'),
            recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.ingredient.insert(
            quantity='.25',
            unit='cup',
            ingredient=db.ingredientName(name='diced green chiles, drained'),
            recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.ingredient.insert(
            quantity='1',
            unit='cup',
            ingredient=db.ingredientName(name='grated Parmesan cheese'),
            recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.ingredient.insert(
            quantity='1',
            unit='dash',
            ingredient=db.ingredientName(name='salt'),
            recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    
    
#########################################
#  COLLECTION - RECIPES                 #
#########################################
if db(db.collection_recipes.id > 0).count() == 0:
    db.collection_recipes.insert(
        collection= db.collection(name='My Test Collection'),
        recipe=db.recipe(name='Too Much Chocolate Cake')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='My Test Collection'),
        recipe=db.recipe(name='Chocolate Chocolate Chip Cookies')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='My Test Collection'),
        recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='My Thanksgiving Dinner'),
        recipe=db.recipe(name='Parmesan Crusted Chicken')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='My Thanksgiving Dinner'),
        recipe=db.recipe(name='Chicken Pot Pie')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='My Thanksgiving Dinner'),
        recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='Conflicting Ingredients'),
        recipe=db.recipe(name='Double Chili Cheese Dip')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='Conflicting Ingredients'),
        recipe=db.recipe(name='Arcadian Eight Bean Chili')
    )
    db.collection_recipes.insert(
        collection= db.collection(name='Conflicting Ingredients'),
        recipe=db.recipe(name='Parmesan Crusted Chicken')
    )
    