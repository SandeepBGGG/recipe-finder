# recipes.py
# Recipe data and matching logic for the Recipe Finder app.

RECIPES = {
    "Butter Chicken": {
        "ingredients": ["Chicken", "Butter", "Tomato Puree", "Heavy Cream", "Garlic Ginger Paste", "Kasuri Methi", "Garam Masala"],
        "instructions": [
            "Marinate chicken in yogurt and spices, then grill it.",
            "Cook tomato puree with ginger-garlic paste and butter.",
            "Add heavy cream and grilled chicken to the gravy.",
            "Simmer and garnish with kasuri methi.",
        ],
    },
    "Paneer Butter Masala": {
        "ingredients": ["Paneer", "Tomato", "Butter", "Heavy Cream", "Ginger", "Garlic", "Cashews", "Garam Masala"],
        "instructions": [
            "Blend tomatoes, ginger, garlic, and soaked cashews into a smooth puree.",
            "Cook the puree in butter with garam masala until thick.",
            "Stir in cream and paneer, then simmer for 5 minutes.",
            "Serve warm with rice or naan.",
        ],
    },
    "Chana Masala": {
        "ingredients": ["Chickpeas", "Tomato", "Onion", "Garlic", "Ginger", "Cumin", "Garam Masala"],
        "instructions": [
            "Cook chopped onion until soft, then add garlic and ginger.",
            "Stir in cumin, garam masala, and chopped tomato.",
            "Add chickpeas and a splash of water, then simmer for 15 minutes.",
            "Season to taste and serve with rice or flatbread.",
        ],
    },
    "Dal Tadka": {
        "ingredients": ["Lentils", "Onion", "Tomato", "Garlic", "Ginger", "Cumin", "Butter"],
        "instructions": [
            "Rinse lentils and simmer in water until tender.",
            "Cook onion, tomato, ginger, and garlic in butter until soft.",
            "Stir the spiced mixture into the lentils and simmer for 5 minutes.",
            "Adjust the seasoning and serve with rice.",
        ],
    },
    "Aloo Gobi": {
        "ingredients": ["Potato", "Cauliflower", "Onion", "Tomato", "Ginger", "Cumin", "Turmeric"],
        "instructions": [
            "Cut the potato and cauliflower into bite-sized pieces.",
            "Cook cumin and onion in a little oil until fragrant.",
            "Add potato, cauliflower, tomato, ginger, and turmeric.",
            "Cover and cook until tender, stirring occasionally.",
        ],
    },
    "Chicken Tikka": {
        "ingredients": ["Chicken", "Yogurt", "Lemon", "Garlic", "Ginger", "Paprika", "Garam Masala"],
        "instructions": [
            "Mix yogurt, lemon juice, garlic, ginger, paprika, and garam masala.",
            "Coat chicken pieces in the marinade and chill for at least 30 minutes.",
            "Thread chicken onto skewers and grill or roast until cooked through.",
            "Serve with lemon wedges and your favorite side.",
        ],
    },
    "Chicken Curry": {
        "ingredients": ["Chicken", "Onion", "Tomato", "Garlic", "Ginger", "Curry Powder", "Coconut Milk"],
        "instructions": [
            "Brown chicken pieces in a little oil, then set aside.",
            "Cook onion, garlic, and ginger until soft.",
            "Stir in curry powder and tomato, then add chicken and coconut milk.",
            "Simmer until the chicken is cooked through and the sauce thickens.",
        ],
    },
    "Chicken Fried Rice": {
        "ingredients": ["Chicken", "Rice", "Egg", "Carrot", "Peas", "Soy Sauce", "Green Onion"],
        "instructions": [
            "Cook diced chicken in a hot pan until fully cooked, then set aside.",
            "Scramble the egg, then add carrot and peas and cook until tender.",
            "Add cooked rice, chicken, and soy sauce and stir-fry until hot.",
            "Top with sliced green onion and serve.",
        ],
    },
    "Vegetable Fried Rice": {
        "ingredients": ["Rice", "Egg", "Carrot", "Peas", "Soy Sauce", "Garlic", "Green Onion"],
        "instructions": [
            "Scramble the egg in a hot pan and set aside.",
            "Cook garlic, carrot, and peas until tender.",
            "Add cooked rice, egg, and soy sauce and stir-fry until hot.",
            "Garnish with sliced green onion.",
        ],
    },
    "Spaghetti Bolognese": {
        "ingredients": ["Spaghetti", "Ground Beef", "Tomato", "Onion", "Garlic", "Olive Oil", "Parmesan"],
        "instructions": [
            "Boil spaghetti in salted water until tender.",
            "Cook onion and garlic in olive oil, then brown the ground beef.",
            "Add tomato and simmer the sauce for 20 minutes.",
            "Serve the sauce over spaghetti with grated Parmesan.",
        ],
    },
    "Creamy Tomato Pasta": {
        "ingredients": ["Pasta", "Tomato", "Heavy Cream", "Garlic", "Onion", "Parmesan", "Olive Oil"],
        "instructions": [
            "Cook pasta according to the package directions.",
            "Cook onion and garlic in olive oil, then add chopped tomato.",
            "Simmer until soft, stir in cream, and season to taste.",
            "Toss with pasta and Parmesan.",
        ],
    },
    "Pesto Pasta": {
        "ingredients": ["Pasta", "Basil", "Parmesan", "Pine Nuts", "Garlic", "Olive Oil"],
        "instructions": [
            "Cook pasta according to the package directions and reserve a little pasta water.",
            "Blend basil, Parmesan, pine nuts, garlic, and olive oil into a pesto.",
            "Toss the pasta with pesto, adding pasta water to loosen the sauce.",
            "Serve with extra Parmesan.",
        ],
    },
    "Mac and Cheese": {
        "ingredients": ["Macaroni", "Cheddar Cheese", "Milk", "Butter", "Flour"],
        "instructions": [
            "Boil macaroni until tender and drain.",
            "Melt butter, stir in flour, and cook for 1 minute.",
            "Whisk in milk and cook until thick, then melt in cheddar.",
            "Fold in macaroni and serve warm.",
        ],
    },
    "Margherita Pizza": {
        "ingredients": ["Pizza Dough", "Tomato Sauce", "Mozzarella", "Basil", "Olive Oil"],
        "instructions": [
            "Heat the oven to its highest setting and stretch the pizza dough.",
            "Spread a thin layer of tomato sauce over the dough.",
            "Add mozzarella and bake until the crust is golden.",
            "Top with fresh basil and a drizzle of olive oil.",
        ],
    },
    "Grilled Cheese Sandwich": {
        "ingredients": ["Bread", "Cheddar Cheese", "Butter"],
        "instructions": [
            "Butter one side of each slice of bread.",
            "Place cheese between the unbuttered sides of the bread.",
            "Cook in a pan over medium heat until golden on both sides and the cheese melts.",
            "Slice and serve warm.",
        ],
    },
    "Tomato Soup": {
        "ingredients": ["Tomato", "Onion", "Garlic", "Vegetable Stock", "Heavy Cream", "Butter"],
        "instructions": [
            "Cook onion and garlic in butter until soft.",
            "Add tomatoes and vegetable stock, then simmer for 20 minutes.",
            "Blend until smooth and stir in cream.",
            "Season to taste and serve hot.",
        ],
    },
    "Vegetable Omelette": {
        "ingredients": ["Egg", "Bell Pepper", "Onion", "Cheddar Cheese", "Butter"],
        "instructions": [
            "Beat the eggs and chop the bell pepper and onion.",
            "Cook the vegetables in butter until tender.",
            "Pour in the eggs and cook gently until nearly set.",
            "Add cheddar, fold the omelette, and serve.",
        ],
    },
    "Pancakes": {
        "ingredients": ["Flour", "Milk", "Egg", "Sugar", "Butter", "Baking Powder"],
        "instructions": [
            "Whisk flour, sugar, and baking powder in a bowl.",
            "Whisk in milk, egg, and melted butter until just combined.",
            "Pour batter onto a warm greased pan and cook until bubbles appear.",
            "Flip and cook the other side until golden.",
        ],
    },
    "French Toast": {
        "ingredients": ["Bread", "Egg", "Milk", "Cinnamon", "Butter", "Sugar"],
        "instructions": [
            "Whisk egg, milk, cinnamon, and sugar in a shallow bowl.",
            "Dip each slice of bread in the mixture.",
            "Cook in butter over medium heat until golden on both sides.",
            "Serve warm with your favorite topping.",
        ],
    },
    "Caesar Salad": {
        "ingredients": ["Romaine Lettuce", "Parmesan", "Croutons", "Mayonnaise", "Lemon", "Garlic"],
        "instructions": [
            "Whisk mayonnaise, lemon juice, and crushed garlic into a dressing.",
            "Toss chopped romaine lettuce with the dressing.",
            "Add croutons and shaved Parmesan.",
            "Serve immediately.",
        ],
    },
    "Greek Salad": {
        "ingredients": ["Cucumber", "Tomato", "Red Onion", "Feta Cheese", "Olives", "Olive Oil"],
        "instructions": [
            "Chop cucumber and tomato and thinly slice the red onion.",
            "Combine the vegetables with olives and crumbled feta.",
            "Drizzle with olive oil and season to taste.",
            "Toss gently and serve.",
        ],
    },
    "Guacamole": {
        "ingredients": ["Avocado", "Lime", "Tomato", "Red Onion", "Cilantro", "Salt"],
        "instructions": [
            "Mash ripe avocado with lime juice.",
            "Fold in diced tomato, red onion, and chopped cilantro.",
            "Season with salt and add more lime if desired.",
            "Serve with tortilla chips or as a topping.",
        ],
    },
    "Beef Tacos": {
        "ingredients": ["Ground Beef", "Taco Shells", "Lettuce", "Tomato", "Cheddar Cheese", "Taco Seasoning"],
        "instructions": [
            "Brown ground beef in a pan and drain excess fat.",
            "Stir in taco seasoning and a splash of water, then simmer briefly.",
            "Fill taco shells with beef, lettuce, and tomato.",
            "Top with grated cheddar and serve.",
        ],
    },
    "Chicken Quesadilla": {
        "ingredients": ["Chicken", "Tortilla", "Cheddar Cheese", "Bell Pepper", "Onion"],
        "instructions": [
            "Cook diced chicken with sliced bell pepper and onion.",
            "Place chicken and vegetables on half of a tortilla and top with cheese.",
            "Fold the tortilla and toast in a pan until golden on both sides.",
            "Cut into wedges and serve warm.",
        ],
    },
    "Lentil Soup": {
        "ingredients": ["Lentils", "Carrot", "Celery", "Onion", "Vegetable Stock", "Tomato"],
        "instructions": [
            "Chop the carrot, celery, and onion.",
            "Cook the vegetables until softened, then add lentils and tomato.",
            "Pour in vegetable stock and simmer until the lentils are tender.",
            "Season to taste and serve hot.",
        ],
    },
    "Mushroom Risotto": {
        "ingredients": ["Arborio Rice", "Mushroom", "Onion", "Vegetable Stock", "Parmesan", "Butter"],
        "instructions": [
            "Cook sliced mushrooms and onion in butter until softened.",
            "Stir in Arborio rice and add warm stock a ladle at a time.",
            "Keep stirring and adding stock until the rice is creamy and tender.",
            "Stir in Parmesan and serve.",
        ],
    },
    "Baked Salmon": {
        "ingredients": ["Salmon", "Lemon", "Garlic", "Olive Oil", "Dill"],
        "instructions": [
            "Heat the oven to 200 C (400 F) and place salmon on a lined tray.",
            "Brush with olive oil and season with garlic and dill.",
            "Bake until the salmon flakes easily, about 12 to 15 minutes.",
            "Serve with lemon wedges.",
        ],
    },
    "Garlic Butter Shrimp": {
        "ingredients": ["Shrimp", "Butter", "Garlic", "Lemon", "Parsley"],
        "instructions": [
            "Melt butter in a pan and cook minced garlic briefly.",
            "Add shrimp and cook until pink and opaque, turning once.",
            "Add lemon juice and chopped parsley.",
            "Serve immediately with bread or rice.",
        ],
    },
    "Baked Potato": {
        "ingredients": ["Potato", "Olive Oil", "Salt", "Cheddar Cheese", "Sour Cream"],
        "instructions": [
            "Heat the oven to 220 C (425 F) and scrub the potato.",
            "Rub with olive oil and salt, then bake until tender.",
            "Split the potato and fluff the inside with a fork.",
            "Top with cheddar and sour cream.",
        ],
    },
    "Chocolate Brownies": {
        "ingredients": ["Dark Chocolate", "Butter", "Sugar", "Egg", "Flour", "Cocoa Powder"],
        "instructions": [
            "Heat the oven to 180 C (350 F) and line a baking pan.",
            "Melt chocolate and butter, then whisk in sugar and eggs.",
            "Fold in flour and cocoa powder until just combined.",
            "Bake until the center is just set, then cool before slicing.",
        ],
    },
    "Banana Smoothie": {
        "ingredients": ["Banana", "Milk", "Yogurt", "Honey"],
        "instructions": [
            "Peel the banana and add it to a blender.",
            "Add milk, yogurt, and honey.",
            "Blend until smooth.",
            "Pour into a glass and serve cold.",
        ],
    },
    "Aloo Paratha": {
        "ingredients": ["Whole Wheat Flour", "Potato", "Green Chili", "Cumin", "Cilantro", "Butter"],
        "instructions": [
            "Knead whole wheat flour with water and a pinch of salt into a soft dough.",
            "Mash cooked potato with green chili, cumin, cilantro, and salt; fill dough balls and roll flat.",
            "Cook on a hot pan with butter until golden on both sides.",
        ],
    },
    "Gobi Paratha": {
        "ingredients": ["Whole Wheat Flour", "Cauliflower", "Ginger", "Green Chili", "Cumin", "Ghee"],
        "instructions": [
            "Knead whole wheat flour with water and salt into a soft dough.",
            "Grate cauliflower and mix with ginger, green chili, cumin, and salt; stuff and roll the dough.",
            "Pan-cook with ghee until both sides are golden and the filling is hot.",
        ],
    },
    "Mooli Paratha": {
        "ingredients": ["Whole Wheat Flour", "Daikon Radish", "Green Chili", "Cilantro", "Carom Seeds", "Ghee"],
        "instructions": [
            "Knead whole wheat flour with water and salt into a soft dough.",
            "Grate and squeeze the radish, then mix with green chili, cilantro, carom seeds, and salt.",
            "Fill and roll the dough, then cook with ghee until golden on both sides.",
        ],
    },
    "Paneer Paratha": {
        "ingredients": ["Whole Wheat Flour", "Paneer", "Green Chili", "Cilantro", "Garam Masala", "Ghee"],
        "instructions": [
            "Knead whole wheat flour with water and salt into a soft dough.",
            "Crumble paneer and mix with green chili, cilantro, garam masala, and salt.",
            "Stuff and roll the dough, then cook with ghee until golden on both sides.",
        ],
    },
    "Chole Bhature": {
        "ingredients": ["Chickpeas", "Onion", "Tomato", "Ginger", "Chole Masala", "Flour", "Yogurt"],
        "instructions": [
            "Soak chickpeas overnight and pressure-cook until tender.",
            "Cook onion, ginger, tomato, and chole masala; add chickpeas and simmer until thick.",
            "Make a yogurt-based flour dough, rest it, roll into discs, and deep-fry until puffed.",
        ],
    },
    "Rajma Masala": {
        "ingredients": ["Kidney Beans", "Onion", "Tomato", "Ginger", "Garlic", "Cumin", "Garam Masala"],
        "instructions": [
            "Soak kidney beans overnight, then pressure-cook until completely tender.",
            "Cook cumin, onion, ginger, and garlic until soft; add tomato and garam masala.",
            "Add beans and some cooking liquid, then simmer until the gravy thickens.",
        ],
    },
    "Kadhi Pakora": {
        "ingredients": ["Yogurt", "Gram Flour", "Onion", "Fenugreek Seeds", "Turmeric", "Cumin", "Chili Powder"],
        "instructions": [
            "Whisk yogurt, gram flour, turmeric, and water until smooth, then simmer gently until thick.",
            "Make an onion and gram flour batter, shape into small fritters, and fry until golden.",
            "Add the fritters to the kadhi and finish with a cumin and chili tempering.",
        ],
    },
    "Palak Paneer": {
        "ingredients": ["Spinach", "Paneer", "Onion", "Tomato", "Garlic", "Ginger", "Garam Masala"],
        "instructions": [
            "Blanch spinach briefly, cool it, and blend into a smooth puree.",
            "Cook onion, garlic, ginger, tomato, and garam masala until soft.",
            "Stir in spinach and paneer cubes; simmer gently until heated through.",
        ],
    },
    "Shahi Paneer": {
        "ingredients": ["Paneer", "Onion", "Tomato", "Cashews", "Heavy Cream", "Cardamom", "Garam Masala"],
        "instructions": [
            "Cook onion, tomato, and cashews until soft, then blend into a smooth sauce.",
            "Simmer the sauce with cardamom and garam masala until creamy.",
            "Add paneer and cream, then cook gently for a few minutes.",
        ],
    },
    "Kadai Paneer": {
        "ingredients": ["Paneer", "Bell Pepper", "Tomato", "Onion", "Coriander Seeds", "Ginger", "Kashmiri Chili"],
        "instructions": [
            "Coarsely crush coriander seeds and Kashmiri chili.",
            "Cook onion, ginger, tomato, and the spice mix until the tomatoes soften.",
            "Add bell pepper and paneer; cook until tender but still holding its shape.",
        ],
    },
    "Matar Paneer": {
        "ingredients": ["Paneer", "Peas", "Tomato", "Onion", "Ginger", "Cumin", "Garam Masala"],
        "instructions": [
            "Cook cumin, onion, and ginger until fragrant, then add tomato and garam masala.",
            "Simmer the sauce until thick and blend if a smooth gravy is preferred.",
            "Add peas and paneer with a little water; simmer until the peas are tender.",
        ],
    },
    "Paneer Bhurji": {
        "ingredients": ["Paneer", "Onion", "Tomato", "Green Chili", "Turmeric", "Cumin", "Cilantro"],
        "instructions": [
            "Crumble paneer and finely chop the onion, tomato, and green chili.",
            "Cook cumin, onion, and chili; add tomato and turmeric and cook until soft.",
            "Fold in paneer, warm through, and finish with chopped cilantro.",
        ],
    },
    "Malai Kofta": {
        "ingredients": ["Paneer", "Potato", "Corn Flour", "Tomato", "Cashews", "Heavy Cream", "Garam Masala"],
        "instructions": [
            "Mash paneer and cooked potato, shape into balls, coat lightly with corn flour, and fry until golden.",
            "Cook tomato and cashews until soft, blend, and simmer with garam masala.",
            "Stir cream into the sauce and add the koftas just before serving.",
        ],
    },
    "Navratan Korma": {
        "ingredients": ["Carrot", "Peas", "Potato", "Cauliflower", "Cashews", "Yogurt", "Heavy Cream"],
        "instructions": [
            "Chop the vegetables and simmer or steam them until just tender.",
            "Blend cashews with yogurt and a little water into a smooth sauce.",
            "Simmer the sauce with the vegetables, then finish with cream.",
        ],
    },
    "Baingan Bharta": {
        "ingredients": ["Eggplant", "Onion", "Tomato", "Garlic", "Green Chili", "Cumin", "Cilantro"],
        "instructions": [
            "Roast the eggplant until collapsed and charred, then peel and mash it.",
            "Cook cumin, onion, garlic, and green chili until soft; add tomato.",
            "Stir in the mashed eggplant and cook until thick; finish with cilantro.",
        ],
    },
    "Bhindi Masala": {
        "ingredients": ["Okra", "Onion", "Tomato", "Cumin", "Coriander Powder", "Turmeric", "Amchur"],
        "instructions": [
            "Wash and thoroughly dry the okra, then slice it.",
            "Pan-fry okra until lightly browned and set aside.",
            "Cook cumin, onion, tomato, coriander, and turmeric; return okra and finish with amchur.",
        ],
    },
    "Bharwa Bhindi": {
        "ingredients": ["Okra", "Gram Flour", "Coriander Powder", "Fennel Seeds", "Amchur", "Turmeric", "Oil"],
        "instructions": [
            "Slit each dry okra lengthwise without cutting all the way through.",
            "Mix gram flour with coriander, ground fennel, amchur, turmeric, and salt; stuff the okra.",
            "Cook covered in a little oil over low heat, turning gently until tender.",
        ],
    },
    "Dum Aloo": {
        "ingredients": ["Baby Potatoes", "Yogurt", "Tomato", "Ginger", "Fennel Powder", "Kashmiri Chili", "Garam Masala"],
        "instructions": [
            "Parboil baby potatoes, prick them, and lightly brown them in a pan.",
            "Cook tomato, ginger, fennel, Kashmiri chili, and garam masala into a thick sauce.",
            "Add yogurt and potatoes, cover, and simmer gently until the sauce coats the potatoes.",
        ],
    },
    "Jeera Aloo": {
        "ingredients": ["Potato", "Cumin", "Green Chili", "Turmeric", "Coriander Powder", "Amchur", "Cilantro"],
        "instructions": [
            "Boil potatoes until just tender, cool, peel, and cut into cubes.",
            "Sizzle cumin and green chili in oil, then add turmeric and coriander powder.",
            "Toss in potatoes and amchur; cook until lightly crisp and garnish with cilantro.",
        ],
    },
    "Sarson ka Saag": {
        "ingredients": ["Mustard Greens", "Spinach", "Corn Flour", "Ginger", "Garlic", "Onion", "Butter"],
        "instructions": [
            "Wash and chop mustard greens and spinach, then simmer with ginger and garlic until soft.",
            "Mash or blend the greens coarsely and stir in corn flour to thicken.",
            "Cook onion in butter until golden and stir the tempering into the saag.",
        ],
    },
    "Makki ki Roti": {
        "ingredients": ["Cornmeal", "Warm Water", "Salt", "Ghee"],
        "instructions": [
            "Mix cornmeal and salt, then gradually add warm water to make a soft dough.",
            "Pat portions into flat rounds between damp sheets or with wet hands.",
            "Cook on a hot griddle until browned on both sides and brush with ghee.",
        ],
    },
    "Methi Thepla": {
        "ingredients": ["Whole Wheat Flour", "Fenugreek Leaves", "Yogurt", "Turmeric", "Chili Powder", "Sesame Seeds", "Oil"],
        "instructions": [
            "Mix flour with chopped fenugreek, yogurt, turmeric, chili powder, sesame, and salt.",
            "Add water as needed, knead into a soft dough, and roll into thin rounds.",
            "Cook each round on a hot griddle with a little oil until spotted on both sides.",
        ],
    },
    "Gujarati Dhokla": {
        "ingredients": ["Gram Flour", "Yogurt", "Lemon Juice", "Eno Fruit Salt", "Mustard Seeds", "Green Chili", "Curry Leaves"],
        "instructions": [
            "Whisk gram flour, yogurt, water, lemon juice, and salt into a smooth batter.",
            "Fold in fruit salt, pour into a greased pan, and steam until a tester comes out clean.",
            "Temper mustard seeds, green chili, and curry leaves in oil and pour over the cut dhokla.",
        ],
    },
    "Khandvi": {
        "ingredients": ["Gram Flour", "Yogurt", "Turmeric", "Mustard Seeds", "Sesame Seeds", "Coconut", "Cilantro"],
        "instructions": [
            "Whisk gram flour, yogurt, turmeric, salt, and water until smooth.",
            "Cook while stirring constantly until very thick, then spread thinly over a flat surface.",
            "Once cool, roll into strips and top with a mustard seed, sesame, coconut, and cilantro tempering.",
        ],
    },
    "Undhiyu": {
        "ingredients": ["Purple Yam", "Sweet Potato", "Eggplant", "Green Beans", "Peas", "Coconut", "Cilantro"],
        "instructions": [
            "Chop the vegetables and mix grated coconut with cilantro, green chili, and spices.",
            "Stuff small eggplants and potatoes with some of the coconut mixture.",
            "Layer all vegetables in a pot with the remaining mixture and steam until tender.",
        ],
    },
    "Pav Bhaji": {
        "ingredients": ["Potato", "Cauliflower", "Peas", "Tomato", "Onion", "Pav Bhaji Masala", "Pav Bread"],
        "instructions": [
            "Boil potato, cauliflower, and peas until soft, then mash them.",
            "Cook onion and tomato with pav bhaji masala; add the vegetables and mash together on the pan.",
            "Toast pav bread with butter and serve alongside the bhaji.",
        ],
    },
    "Vada Pav": {
        "ingredients": ["Potato", "Gram Flour", "Green Chili", "Garlic", "Mustard Seeds", "Pav Bread", "Chutney"],
        "instructions": [
            "Mash cooked potato with chili, garlic, mustard seeds, and salt; shape into balls.",
            "Dip each ball in seasoned gram flour batter and deep-fry until golden.",
            "Split pav bread, add chutney and a potato vada, then serve hot.",
        ],
    },
    "Misal Pav": {
        "ingredients": ["Sprouted Mung Beans", "Onion", "Tomato", "Misal Masala", "Farsan", "Cilantro", "Pav Bread"],
        "instructions": [
            "Cook sprouted mung beans until tender.",
            "Simmer onion, tomato, and misal masala with water to make a spicy broth, then add the sprouts.",
            "Top with farsan, chopped onion, and cilantro; serve with pav bread.",
        ],
    },
    "Poha": {
        "ingredients": ["Flattened Rice", "Onion", "Peas", "Mustard Seeds", "Turmeric", "Peanuts", "Lemon"],
        "instructions": [
            "Rinse flattened rice briefly and let it drain until soft but not mushy.",
            "Sizzle mustard seeds, cook onion and peas, then stir in turmeric and peanuts.",
            "Fold in the flattened rice, warm through, and finish with lemon juice.",
        ],
    },
    "Upma": {
        "ingredients": ["Semolina", "Onion", "Green Chili", "Mustard Seeds", "Curry Leaves", "Cashews", "Water"],
        "instructions": [
            "Dry-roast semolina in a pan until fragrant and set aside.",
            "Temper mustard seeds, curry leaves, chili, onion, and cashews in oil.",
            "Add water and salt; when boiling, slowly stir in semolina and cook until fluffy.",
        ],
    },
    "Idli": {
        "ingredients": ["Idli Rice", "Urad Dal", "Fenugreek Seeds", "Salt", "Water"],
        "instructions": [
            "Soak rice and urad dal separately with fenugreek, then grind to a smooth batter.",
            "Mix the batters and ferment in a warm place until airy.",
            "Pour into greased idli molds and steam until cooked through.",
        ],
    },
    "Medu Vada": {
        "ingredients": ["Urad Dal", "Black Pepper", "Cumin", "Curry Leaves", "Green Chili", "Ginger", "Oil"],
        "instructions": [
            "Soak urad dal, drain very well, and grind with minimal water into a fluffy batter.",
            "Fold in pepper, cumin, curry leaves, chili, ginger, and salt.",
            "Shape into rings with wet hands and deep-fry until crisp and golden.",
        ],
    },
    "Masala Dosa": {
        "ingredients": ["Dosa Batter", "Potato", "Onion", "Mustard Seeds", "Curry Leaves", "Turmeric", "Ghee"],
        "instructions": [
            "Cook potato with onion, mustard seeds, curry leaves, and turmeric to make the filling.",
            "Spread dosa batter thinly on a hot greased griddle.",
            "Cook until crisp, add the potato filling, fold, and serve.",
        ],
    },
    "Rava Dosa": {
        "ingredients": ["Semolina", "Rice Flour", "All-Purpose Flour", "Cumin", "Green Chili", "Onion", "Water"],
        "instructions": [
            "Whisk semolina, rice flour, all-purpose flour, cumin, salt, and plenty of water into a thin batter.",
            "Stir in chopped green chili and onion, then rest the batter briefly.",
            "Pour the batter in a thin lacy layer on a hot pan and cook until crisp.",
        ],
    },
    "Uttapam": {
        "ingredients": ["Dosa Batter", "Onion", "Tomato", "Green Chili", "Cilantro", "Bell Pepper", "Oil"],
        "instructions": [
            "Chop onion, tomato, green chili, cilantro, and bell pepper.",
            "Pour a thick round of dosa batter onto a warm greased griddle.",
            "Scatter vegetables over the top, cook until set, then flip and cook through.",
        ],
    },
    "Sambar": {
        "ingredients": ["Toor Dal", "Drumstick", "Carrot", "Tomato", "Tamarind", "Sambar Powder", "Curry Leaves"],
        "instructions": [
            "Cook toor dal until soft and simmer chopped vegetables until tender.",
            "Add tamarind water, sambar powder, and cooked dal; simmer until flavors combine.",
            "Temper mustard seeds and curry leaves in oil and stir into the sambar.",
        ],
    },
    "Rasam": {
        "ingredients": ["Tomato", "Tamarind", "Toor Dal", "Black Pepper", "Cumin", "Garlic", "Curry Leaves"],
        "instructions": [
            "Simmer tamarind water with chopped tomato, crushed pepper, cumin, and garlic.",
            "Stir in a little cooked toor dal and heat until fragrant without boiling vigorously.",
            "Temper mustard seeds and curry leaves in oil and pour over the rasam.",
        ],
    },
    "Lemon Rice": {
        "ingredients": ["Rice", "Lemon", "Peanuts", "Mustard Seeds", "Turmeric", "Curry Leaves", "Green Chili"],
        "instructions": [
            "Cook rice until fluffy and let it cool slightly.",
            "Temper mustard seeds, peanuts, curry leaves, chili, and turmeric in oil.",
            "Fold the tempering and fresh lemon juice through the rice.",
        ],
    },
    "Curd Rice": {
        "ingredients": ["Rice", "Yogurt", "Milk", "Mustard Seeds", "Curry Leaves", "Ginger", "Pomegranate"],
        "instructions": [
            "Cook rice until very soft, mash lightly, and let it cool.",
            "Mix in yogurt, a little milk, grated ginger, and salt.",
            "Temper mustard seeds and curry leaves in oil; add as a topping with pomegranate.",
        ],
    },
    "Tamarind Rice": {
        "ingredients": ["Rice", "Tamarind", "Peanuts", "Sesame Seeds", "Mustard Seeds", "Curry Leaves", "Turmeric"],
        "instructions": [
            "Cook rice and let the grains cool separately.",
            "Simmer tamarind pulp with turmeric, roasted sesame, and salt until thick.",
            "Temper mustard seeds, peanuts, and curry leaves; mix with the tamarind paste and rice.",
        ],
    },
    "Vegetable Biryani": {
        "ingredients": ["Basmati Rice", "Carrot", "Potato", "Peas", "Yogurt", "Biryani Masala", "Mint"],
        "instructions": [
            "Rinse and soak basmati rice; parboil it with whole spices and drain.",
            "Cook chopped vegetables with yogurt, biryani masala, and mint until partly tender.",
            "Layer rice over the vegetables, cover tightly, and steam on low heat until done.",
        ],
    },
    "Hyderabadi Chicken Biryani": {
        "ingredients": ["Chicken", "Basmati Rice", "Yogurt", "Fried Onion", "Biryani Masala", "Mint", "Saffron"],
        "instructions": [
            "Marinate chicken in yogurt, biryani masala, ginger-garlic, mint, and fried onion.",
            "Parboil soaked basmati rice with whole spices and drain.",
            "Layer rice over chicken, add saffron milk, cover tightly, and cook until chicken and rice are done.",
        ],
    },
    "Egg Biryani": {
        "ingredients": ["Egg", "Basmati Rice", "Onion", "Tomato", "Yogurt", "Biryani Masala", "Mint"],
        "instructions": [
            "Boil and peel eggs, then score and lightly brown them with biryani spices.",
            "Cook onion and tomato with yogurt and biryani masala; add the eggs.",
            "Layer with parboiled basmati rice and mint, cover, and steam until fragrant.",
        ],
    },
    "Peas Pulao": {
        "ingredients": ["Basmati Rice", "Peas", "Onion", "Cumin", "Cardamom", "Cinnamon", "Ghee"],
        "instructions": [
            "Rinse and soak basmati rice, then drain.",
            "Warm ghee and cook cumin, cardamom, cinnamon, and sliced onion until fragrant.",
            "Add peas, rice, water, and salt; cover and cook until the rice is fluffy.",
        ],
    },
    "Coconut Rice": {
        "ingredients": ["Rice", "Grated Coconut", "Mustard Seeds", "Urad Dal", "Cashews", "Curry Leaves", "Green Chili"],
        "instructions": [
            "Cook rice until fluffy and allow it to cool.",
            "Temper mustard seeds, urad dal, cashews, chili, and curry leaves in oil.",
            "Stir in grated coconut, warm briefly, then fold through the rice with salt.",
        ],
    },
    "Appam": {
        "ingredients": ["Raw Rice", "Cooked Rice", "Coconut Milk", "Yeast", "Sugar", "Salt"],
        "instructions": [
            "Soak raw rice and grind with cooked rice and coconut milk into a smooth batter.",
            "Mix in activated yeast, sugar, and salt; cover and ferment until bubbly.",
            "Pour batter into an appam pan, swirl to make thin edges, cover, and cook until set.",
        ],
    },
    "Kerala Vegetable Stew": {
        "ingredients": ["Potato", "Carrot", "Green Beans", "Coconut Milk", "Onion", "Ginger", "Curry Leaves"],
        "instructions": [
            "Cook potato, carrot, and green beans with sliced onion and ginger until tender.",
            "Add thin coconut milk and simmer gently with salt and black pepper.",
            "Stir in thick coconut milk and curry leaves; warm gently without boiling.",
        ],
    },
    "Kerala Fish Curry": {
        "ingredients": ["Fish", "Coconut Milk", "Tamarind", "Shallot", "Ginger", "Kashmiri Chili", "Curry Leaves"],
        "instructions": [
            "Soak tamarind in warm water and slice the shallot and ginger.",
            "Cook shallot, ginger, and Kashmiri chili; add tamarind water and coconut milk.",
            "Add fish pieces and simmer gently until just cooked; finish with curry leaves.",
        ],
    },
    "Meen Fry": {
        "ingredients": ["Fish", "Kashmiri Chili", "Turmeric", "Black Pepper", "Lemon", "Rice Flour", "Coconut Oil"],
        "instructions": [
            "Mix Kashmiri chili, turmeric, pepper, lemon juice, and salt into a paste.",
            "Coat fish pieces and let them marinate briefly.",
            "Dust lightly with rice flour and pan-fry in coconut oil until crisp and cooked through.",
        ],
    },
    "Goan Prawn Curry": {
        "ingredients": ["Prawns", "Coconut Milk", "Tamarind", "Onion", "Garlic", "Kashmiri Chili", "Coriander Seeds"],
        "instructions": [
            "Blend coconut, Kashmiri chili, coriander seeds, garlic, and tamarind into a smooth masala.",
            "Cook sliced onion until soft, then stir in the masala and simmer briefly.",
            "Add prawns and coconut milk; simmer gently until the prawns are cooked.",
        ],
    },
    "Goan Fish Curry": {
        "ingredients": ["Fish", "Coconut", "Kashmiri Chili", "Coriander Seeds", "Tamarind", "Onion", "Turmeric"],
        "instructions": [
            "Blend coconut, Kashmiri chili, coriander, turmeric, and tamarind with water.",
            "Simmer the masala with sliced onion until the raw aroma fades.",
            "Add fish pieces and cook gently until opaque and flaky.",
        ],
    },
    "Chicken Chettinad": {
        "ingredients": ["Chicken", "Onion", "Tomato", "Coconut", "Fennel Seeds", "Black Pepper", "Curry Leaves"],
        "instructions": [
            "Toast coconut, fennel, and black pepper, then grind into a coarse spice paste.",
            "Cook onion and curry leaves, add chicken and tomato, and brown lightly.",
            "Stir in the spice paste and water; cover and simmer until the chicken is tender.",
        ],
    },
    "Chicken Korma": {
        "ingredients": ["Chicken", "Yogurt", "Onion", "Cashews", "Ginger", "Cardamom", "Garam Masala"],
        "instructions": [
            "Blend soaked cashews with yogurt into a smooth paste.",
            "Brown sliced onion, add ginger and chicken, and cook until lightly colored.",
            "Stir in the yogurt paste, cardamom, and garam masala; cover and simmer until tender.",
        ],
    },
    "Chicken 65": {
        "ingredients": ["Chicken", "Yogurt", "Rice Flour", "Corn Flour", "Ginger", "Garlic", "Kashmiri Chili"],
        "instructions": [
            "Marinate chicken pieces in yogurt, ginger, garlic, chili, and salt.",
            "Coat with rice flour and corn flour, then fry until crisp and fully cooked.",
            "Toss with curry leaves and sliced green chili before serving.",
        ],
    },
    "Pepper Chicken": {
        "ingredients": ["Chicken", "Onion", "Black Pepper", "Fennel Seeds", "Ginger", "Garlic", "Curry Leaves"],
        "instructions": [
            "Crush black pepper and fennel seeds; chop onion, ginger, and garlic.",
            "Cook curry leaves, onion, ginger, and garlic until soft, then add chicken.",
            "Season generously with pepper and simmer until the chicken is cooked and coated.",
        ],
    },
    "Mutton Rogan Josh": {
        "ingredients": ["Mutton", "Yogurt", "Onion", "Kashmiri Chili", "Fennel Powder", "Ginger", "Cardamom"],
        "instructions": [
            "Brown mutton pieces in a heavy pot and set aside.",
            "Cook onion with ginger, cardamom, Kashmiri chili, and fennel powder.",
            "Return mutton, add whisked yogurt and water, then cover and simmer until tender.",
        ],
    },
    "Mutton Keema": {
        "ingredients": ["Ground Mutton", "Onion", "Tomato", "Peas", "Ginger", "Garlic", "Garam Masala"],
        "instructions": [
            "Cook onion, ginger, and garlic in oil until golden.",
            "Add ground mutton and brown it thoroughly, breaking up any clumps.",
            "Stir in tomato, peas, and garam masala; cover and cook until tender.",
        ],
    },
    "Laal Maas": {
        "ingredients": ["Mutton", "Yogurt", "Onion", "Kashmiri Chili", "Garlic", "Ghee", "Cumin"],
        "instructions": [
            "Soak dried red chilies in hot water and blend with garlic into a paste.",
            "Brown mutton and onion in ghee, then stir in the chili paste and cumin.",
            "Add yogurt and water, cover, and simmer until the mutton is tender.",
        ],
    },
    "Seekh Kebab": {
        "ingredients": ["Ground Lamb", "Onion", "Ginger", "Garlic", "Cilantro", "Cumin", "Garam Masala"],
        "instructions": [
            "Mix ground lamb with finely chopped onion, ginger, garlic, cilantro, and spices.",
            "Shape the mixture around skewers and chill briefly to help it hold together.",
            "Grill or broil, turning regularly, until browned and cooked through.",
        ],
    },
    "Tandoori Chicken": {
        "ingredients": ["Chicken", "Yogurt", "Lemon", "Ginger", "Garlic", "Tandoori Masala", "Paprika"],
        "instructions": [
            "Score chicken pieces and mix yogurt with lemon, ginger, garlic, tandoori masala, and paprika.",
            "Coat chicken and marinate in the refrigerator for several hours.",
            "Roast or grill, turning once, until charred in spots and cooked through.",
        ],
    },
    "Malai Chicken Tikka": {
        "ingredients": ["Chicken", "Yogurt", "Heavy Cream", "Paneer", "Ginger", "Garlic", "Cardamom"],
        "instructions": [
            "Blend paneer, yogurt, cream, ginger, garlic, cardamom, and salt into a marinade.",
            "Coat chicken cubes and chill for at least 30 minutes.",
            "Thread onto skewers and grill or roast until lightly charred and cooked through.",
        ],
    },
    "Fish Tikka": {
        "ingredients": ["Firm White Fish", "Yogurt", "Lemon", "Ginger", "Garlic", "Turmeric", "Garam Masala"],
        "instructions": [
            "Mix yogurt with lemon, ginger, garlic, turmeric, garam masala, and salt.",
            "Coat fish cubes gently and marinate in the refrigerator for 20 minutes.",
            "Thread onto skewers and grill or roast until opaque and lightly browned.",
        ],
    },
    "Hara Bhara Kebab": {
        "ingredients": ["Spinach", "Peas", "Potato", "Green Chili", "Ginger", "Gram Flour", "Cilantro"],
        "instructions": [
            "Blanch spinach, drain it well, and mash with cooked peas and potato.",
            "Mix in chili, ginger, cilantro, gram flour, and salt; shape into patties.",
            "Shallow-fry the patties until crisp and golden on both sides.",
        ],
    },
    "Dahi Kebab": {
        "ingredients": ["Hung Yogurt", "Paneer", "Gram Flour", "Onion", "Ginger", "Green Chili", "Cilantro"],
        "instructions": [
            "Combine thick hung yogurt with crumbled paneer, finely chopped onion, ginger, chili, and cilantro.",
            "Fold in enough gram flour to form a soft mixture and shape into small patties.",
            "Shallow-fry carefully until browned on both sides and serve hot.",
        ],
    },
    "Samosa": {
        "ingredients": ["All-Purpose Flour", "Potato", "Peas", "Cumin", "Coriander Seeds", "Green Chili", "Oil"],
        "instructions": [
            "Make a firm flour dough with oil, water, and salt; rest it while preparing the filling.",
            "Cook mashed potato and peas with cumin, crushed coriander, chili, and salt.",
            "Fill pastry cones, seal, and deep-fry over medium heat until crisp and golden.",
        ],
    },
    "Onion Pakora": {
        "ingredients": ["Onion", "Gram Flour", "Rice Flour", "Green Chili", "Cilantro", "Carom Seeds", "Oil"],
        "instructions": [
            "Thinly slice onions and mix with chili, cilantro, carom seeds, and salt.",
            "Add gram flour and rice flour with just enough water to coat the onions.",
            "Drop small portions into hot oil and fry until crisp and golden.",
        ],
    },
    "Aloo Tikki": {
        "ingredients": ["Potato", "Green Peas", "Ginger", "Green Chili", "Cumin", "Breadcrumbs", "Oil"],
        "instructions": [
            "Mash cooked potatoes with peas, ginger, chili, cumin, and salt.",
            "Shape into flat patties and coat lightly with breadcrumbs if needed.",
            "Shallow-fry until crisp and golden on both sides.",
        ],
    },
    "Papdi Chaat": {
        "ingredients": ["Papdi", "Potato", "Chickpeas", "Yogurt", "Tamarind Chutney", "Cilantro Chutney", "Sev"],
        "instructions": [
            "Arrange crisp papdi on a serving plate and top with diced cooked potato and chickpeas.",
            "Drizzle with yogurt, tamarind chutney, and cilantro chutney.",
            "Finish with sev, chopped cilantro, and chaat masala; serve immediately.",
        ],
    },
    "Pani Puri": {
        "ingredients": ["Puri Shells", "Potato", "Chickpeas", "Tamarind", "Mint", "Cilantro", "Chaat Masala"],
        "instructions": [
            "Blend mint and cilantro with water, tamarind, chaat masala, and salt to make the spiced pani.",
            "Mash cooked potato and chickpeas with salt and a little chaat masala.",
            "Crack each puri, fill with potato mixture, add pani, and eat at once.",
        ],
    },
    "Bhel Puri": {
        "ingredients": ["Puffed Rice", "Sev", "Onion", "Tomato", "Tamarind Chutney", "Cilantro Chutney", "Peanuts"],
        "instructions": [
            "Combine puffed rice with chopped onion, tomato, and peanuts just before serving.",
            "Toss with tamarind chutney, cilantro chutney, and chaat masala.",
            "Top with sev and chopped cilantro and serve immediately while crisp.",
        ],
    },
    "Dahi Puri": {
        "ingredients": ["Puri Shells", "Potato", "Chickpeas", "Yogurt", "Tamarind Chutney", "Sev", "Cilantro"],
        "instructions": [
            "Arrange puri shells and crack a small opening in each one.",
            "Fill with potato and chickpeas, then spoon in whisked yogurt and tamarind chutney.",
            "Top with sev, cilantro, and chaat masala and serve immediately.",
        ],
    },
    "Kachori": {
        "ingredients": ["All-Purpose Flour", "Moong Dal", "Fennel Seeds", "Coriander Seeds", "Chili Powder", "Oil", "Water"],
        "instructions": [
            "Soak and coarsely grind moong dal; cook with fennel, coriander, chili, and salt until dry.",
            "Make a firm flour dough, fill portions with the dal mixture, and seal into balls.",
            "Flatten gently and deep-fry over low-medium heat until crisp and golden.",
        ],
    },
    "Litti Chokha": {
        "ingredients": ["Whole Wheat Flour", "Sattu", "Eggplant", "Tomato", "Garlic", "Mustard Oil", "Cilantro"],
        "instructions": [
            "Mix sattu with mustard oil, chopped cilantro, lemon, and spices for the filling.",
            "Fill whole wheat dough balls with sattu and bake or roast until browned and cooked through.",
            "Roast eggplant and tomato, mash with garlic and mustard oil, and serve as chokha.",
        ],
    },
    "Sattu Paratha": {
        "ingredients": ["Whole Wheat Flour", "Sattu", "Onion", "Green Chili", "Cilantro", "Mustard Oil", "Lemon"],
        "instructions": [
            "Mix sattu with chopped onion, chili, cilantro, lemon juice, mustard oil, and salt.",
            "Knead whole wheat flour with water into a soft dough and fill portions with the sattu mixture.",
            "Roll gently and cook on a hot griddle with oil until browned on both sides.",
        ],
    },
    "Dal Makhani": {
        "ingredients": ["Whole Black Lentils", "Kidney Beans", "Tomato", "Ginger", "Garlic", "Butter", "Heavy Cream"],
        "instructions": [
            "Soak black lentils and kidney beans overnight, then pressure-cook until very soft.",
            "Cook tomato with ginger and garlic; add the beans and simmer slowly until creamy.",
            "Stir in butter and cream and cook gently until rich and thick.",
        ],
    },
    "Panchmel Dal": {
        "ingredients": ["Toor Dal", "Chana Dal", "Moong Dal", "Masoor Dal", "Urad Dal", "Tomato", "Ghee"],
        "instructions": [
            "Rinse the five lentils and pressure-cook with turmeric until soft.",
            "Simmer the lentils with tomato, water, and salt until the texture is creamy.",
            "Temper cumin and spices in ghee and pour over the dal.",
        ],
    },
    "Moong Dal Khichdi": {
        "ingredients": ["Rice", "Yellow Moong Dal", "Turmeric", "Cumin", "Ghee", "Ginger", "Water"],
        "instructions": [
            "Rinse rice and yellow moong dal together until the water runs mostly clear.",
            "Sizzle cumin and ginger in ghee, then add rice, dal, turmeric, salt, and water.",
            "Cover and cook until soft and porridge-like, adding water if needed.",
        ],
    },
    "Palak Dal": {
        "ingredients": ["Toor Dal", "Spinach", "Tomato", "Onion", "Garlic", "Turmeric", "Cumin"],
        "instructions": [
            "Cook toor dal with turmeric until soft and mash lightly.",
            "Cook onion, garlic, and tomato; add chopped spinach and cook until wilted.",
            "Stir in dal and simmer, then finish with a cumin tempering.",
        ],
    },
    "Gujarati Dal": {
        "ingredients": ["Toor Dal", "Peanuts", "Tomato", "Jaggery", "Tamarind", "Mustard Seeds", "Curry Leaves"],
        "instructions": [
            "Cook toor dal until soft and whisk until smooth.",
            "Simmer with tomato, peanuts, tamarind, jaggery, turmeric, and salt.",
            "Temper mustard seeds and curry leaves in oil and stir into the dal.",
        ],
    },
    "Bengali Aloo Posto": {
        "ingredients": ["Potato", "Poppy Seeds", "Green Chili", "Nigella Seeds", "Turmeric", "Mustard Oil", "Salt"],
        "instructions": [
            "Soak poppy seeds and grind with green chili into a thick paste.",
            "Sizzle nigella seeds in mustard oil, then add cubed potato, turmeric, and salt.",
            "Add a little water and the poppy paste; cover and cook until potatoes are tender.",
        ],
    },
    "Shukto": {
        "ingredients": ["Bitter Melon", "Potato", "Eggplant", "Drumstick", "Mustard Seeds", "Poppy Seeds", "Milk"],
        "instructions": [
            "Cut the vegetables into pieces and lightly fry the bitter melon separately.",
            "Cook the remaining vegetables with a paste of mustard and poppy seeds until tender.",
            "Add milk and the bitter melon, simmer gently, and season to taste.",
        ],
    },
    "Chingri Malai Curry": {
        "ingredients": ["Prawns", "Coconut Milk", "Onion", "Ginger", "Turmeric", "Garam Masala", "Ghee"],
        "instructions": [
            "Season prawns with turmeric and salt, then sear briefly and set aside.",
            "Cook onion and ginger in ghee; add turmeric and coconut milk and simmer.",
            "Return prawns to the sauce and cook gently until just done; finish with garam masala.",
        ],
    },
    "Macher Jhol": {
        "ingredients": ["Fish", "Potato", "Tomato", "Nigella Seeds", "Turmeric", "Green Chili", "Mustard Oil"],
        "instructions": [
            "Season fish with turmeric and salt and lightly fry in mustard oil.",
            "Fry potato pieces, then add nigella seeds, tomato, and green chili.",
            "Add water and simmer until potatoes are tender; return fish and cook briefly.",
        ],
    },
    "Kosha Mangsho": {
        "ingredients": ["Mutton", "Yogurt", "Onion", "Ginger", "Garlic", "Garam Masala", "Mustard Oil"],
        "instructions": [
            "Marinate mutton with yogurt, ginger, garlic, and spices.",
            "Cook sliced onion slowly in mustard oil until deeply golden, then add the mutton.",
            "Cook slowly, stirring often and adding small splashes of water, until tender and richly coated.",
        ],
    },
    "Luchi": {
        "ingredients": ["All-Purpose Flour", "Ghee", "Salt", "Warm Water", "Oil"],
        "instructions": [
            "Rub ghee and salt into the flour, then add warm water and knead a firm dough.",
            "Rest the dough, divide into small balls, and roll into thin discs.",
            "Deep-fry each disc until it puffs, turning once.",
        ],
    },
    "Hyderabadi Haleem": {
        "ingredients": ["Mutton", "Wheat", "Barley", "Lentils", "Ginger", "Garlic", "Ghee"],
        "instructions": [
            "Soak wheat, barley, and lentils, then cook them until very soft.",
            "Cook mutton with ginger, garlic, and spices until tender, then remove bones.",
            "Combine meat and grains and mash or blend to a thick consistency; finish with ghee.",
        ],
    },
    "Keema Matar": {
        "ingredients": ["Ground Beef", "Peas", "Onion", "Tomato", "Ginger", "Garlic", "Cumin"],
        "instructions": [
            "Cook cumin, onion, ginger, and garlic in oil until fragrant.",
            "Add ground beef and brown thoroughly, breaking it into small pieces.",
            "Add tomato, peas, and spices; cover and simmer until the peas are tender.",
        ],
    },
    "Idiyappam": {
        "ingredients": ["Rice Flour", "Boiling Water", "Salt", "Coconut"],
        "instructions": [
            "Mix rice flour and salt, then gradually stir in boiling water to form a soft dough.",
            "Press the dough through an idiyappam maker into greased molds.",
            "Sprinkle with grated coconut and steam until the strands are tender.",
        ],
    },
    "Puttu and Kadala Curry": {
        "ingredients": ["Rice Flour", "Grated Coconut", "Black Chickpeas", "Onion", "Tomato", "Coconut Milk", "Curry Leaves"],
        "instructions": [
            "Moisten rice flour with salted water until crumbly, layer it with coconut in a puttu steamer, and steam.",
            "Cook soaked black chickpeas until tender, then simmer with onion, tomato, spices, and coconut milk.",
            "Serve the steamed puttu with the chickpea curry.",
        ],
    },
    "Assamese Masor Tenga": {
        "ingredients": ["Fish", "Tomato", "Lemon", "Mustard Seeds", "Turmeric", "Green Chili", "Coriander"],
        "instructions": [
            "Season fish with turmeric and salt and lightly fry.",
            "Cook mustard seeds, tomato, and green chili; add water and simmer into a light broth.",
            "Return fish to the broth, add lemon juice, and finish with coriander.",
        ],
    },
    "Thukpa": {
        "ingredients": ["Noodles", "Chicken", "Carrot", "Cabbage", "Onion", "Ginger", "Cilantro"],
        "instructions": [
            "Cook noodles separately according to the package directions.",
            "Simmer chicken with onion, ginger, carrot, cabbage, and water or stock until cooked.",
            "Season the broth, add noodles, and garnish with cilantro.",
        ],
    },
    "Vegetable Momos": {
        "ingredients": ["All-Purpose Flour", "Cabbage", "Carrot", "Onion", "Ginger", "Garlic", "Soy Sauce"],
        "instructions": [
            "Knead flour, water, and salt into a firm dough and rest it.",
            "Stir-fry finely chopped cabbage, carrot, onion, ginger, garlic, and soy sauce until dry.",
            "Fill small dough rounds, pleat closed, and steam until the wrappers are cooked.",
        ],
    },
    "Chicken Momos": {
        "ingredients": ["All-Purpose Flour", "Ground Chicken", "Onion", "Ginger", "Garlic", "Soy Sauce", "Cilantro"],
        "instructions": [
            "Knead flour, water, and salt into a firm dough and rest it.",
            "Mix ground chicken with finely chopped onion, ginger, garlic, soy sauce, and cilantro.",
            "Fill dough rounds, pleat closed, and steam until the chicken filling is fully cooked.",
        ],
    },
    "Indo-Chinese Veg Chow Mein": {
        "ingredients": ["Noodles", "Cabbage", "Carrot", "Bell Pepper", "Soy Sauce", "Vinegar", "Garlic"],
        "instructions": [
            "Boil noodles until just tender, drain, and toss with a little oil.",
            "Stir-fry garlic, cabbage, carrot, and bell pepper over high heat.",
            "Add noodles, soy sauce, and vinegar; toss until hot and serve.",
        ],
    },
    "Chilli Paneer": {
        "ingredients": ["Paneer", "Bell Pepper", "Onion", "Soy Sauce", "Chili Sauce", "Garlic", "Corn Flour"],
        "instructions": [
            "Lightly coat paneer cubes with corn flour and pan-fry until golden.",
            "Stir-fry garlic, onion, and bell pepper over high heat.",
            "Add soy sauce, chili sauce, and paneer; toss until coated and serve.",
        ],
    },
    "Gobi Manchurian": {
        "ingredients": ["Cauliflower", "Corn Flour", "All-Purpose Flour", "Garlic", "Soy Sauce", "Chili Sauce", "Spring Onion"],
        "instructions": [
            "Dip cauliflower florets in a seasoned flour and corn flour batter and fry until crisp.",
            "Cook garlic in a pan, then stir in soy sauce, chili sauce, and a little water.",
            "Toss in the cauliflower until coated and garnish with spring onion.",
        ],
    },
    "Semiya Payasam": {
        "ingredients": ["Vermicelli", "Milk", "Sugar", "Cardamom", "Cashews", "Raisins", "Ghee"],
        "instructions": [
            "Toast vermicelli in ghee until golden.",
            "Add milk and simmer, stirring, until the vermicelli is soft; sweeten with sugar.",
            "Add cardamom and top with cashews and raisins toasted in ghee.",
        ],
    },
    "Rice Kheer": {
        "ingredients": ["Rice", "Milk", "Sugar", "Cardamom", "Almonds", "Pistachios", "Saffron"],
        "instructions": [
            "Rinse rice and simmer it in milk over low heat, stirring frequently.",
            "When the rice is soft and the milk thickens, add sugar, cardamom, and saffron.",
            "Serve warm or chilled, topped with sliced almonds and pistachios.",
        ],
    },
    "Gulab Jamun": {
        "ingredients": ["Milk Powder", "All-Purpose Flour", "Ghee", "Milk", "Sugar", "Cardamom", "Rose Water"],
        "instructions": [
            "Make a soft dough with milk powder, flour, ghee, and enough milk; shape into smooth small balls.",
            "Simmer sugar, water, cardamom, and rose water into a light syrup.",
            "Fry the dough balls over low heat until evenly golden, then soak in warm syrup.",
        ],
    },
    "Besan Ladoo": {
        "ingredients": ["Gram Flour", "Ghee", "Sugar", "Cardamom", "Almonds"],
        "instructions": [
            "Roast gram flour slowly in ghee, stirring constantly until aromatic and golden.",
            "Cool slightly, then mix in powdered sugar, cardamom, and chopped almonds.",
            "Shape the warm mixture into small round ladoos and let them set.",
        ],
    },
    "Bisi Bele Bath": {
        "ingredients": ["Rice", "Toor Dal", "Carrot", "Peas", "Tamarind", "Bisi Bele Bath Masala", "Cashews"],
        "instructions": [
            "Cook rice and toor dal until soft; simmer chopped vegetables until tender.",
            "Combine with tamarind and masala, cook until thick, and top with toasted cashews.",
        ],
    },
    "Vangi Bath": {
        "ingredients": ["Rice", "Eggplant", "Peanuts", "Curry Leaves", "Mustard Seeds", "Vangi Bath Powder", "Tamarind"],
        "instructions": [
            "Cook rice and let it cool; saute eggplant with mustard seeds and curry leaves.",
            "Stir in tamarind and vangi bath powder, then fold through the rice with roasted peanuts.",
        ],
    },
    "Tomato Bath": {
        "ingredients": ["Rice", "Tomato", "Onion", "Ginger", "Green Chili", "Cumin", "Cilantro"],
        "instructions": [
            "Cook onion, ginger, chili, and cumin until fragrant, then add chopped tomato.",
            "Add rinsed rice and water; cover and cook until fluffy, then garnish with cilantro.",
        ],
    },
    "Karnataka Vegetable Sagu": {
        "ingredients": ["Potato", "Carrot", "Peas", "Coconut", "Poppy Seeds", "Green Chili", "Cilantro"],
        "instructions": [
            "Cook chopped vegetables until just tender.",
            "Blend coconut, poppy seeds, chili, and cilantro; simmer the paste with vegetables until creamy.",
        ],
    },
    "Akki Roti": {
        "ingredients": ["Rice Flour", "Onion", "Green Chili", "Cilantro", "Cumin", "Grated Coconut", "Water"],
        "instructions": [
            "Mix rice flour with chopped onion, chili, cilantro, cumin, coconut, salt, and warm water.",
            "Pat into thin rounds on a greased pan and cook on both sides until lightly browned.",
        ],
    },
    "Ragi Mudde": {
        "ingredients": ["Ragi Flour", "Water", "Salt", "Ghee"],
        "instructions": [
            "Bring salted water to a boil and stir in a small amount of ragi flour to make a paste.",
            "Add remaining flour and cook while stirring until firm; shape into balls with a little ghee.",
        ],
    },
    "Neer Dosa": {
        "ingredients": ["Raw Rice", "Coconut", "Water", "Salt", "Oil"],
        "instructions": [
            "Soak rice, then blend with coconut and enough water to make a very thin batter.",
            "Pour onto a hot greased pan, cover until set, and fold gently.",
        ],
    },
    "Pesarattu": {
        "ingredients": ["Whole Mung Beans", "Ginger", "Green Chili", "Cumin", "Onion", "Rice Flour"],
        "instructions": [
            "Soak mung beans, then blend with ginger, chili, cumin, salt, and water into a batter.",
            "Spread thinly on a hot griddle, scatter onion on top, and cook until crisp.",
        ],
    },
    "Adai": {
        "ingredients": ["Rice", "Toor Dal", "Chana Dal", "Urad Dal", "Dried Red Chili", "Curry Leaves", "Onion"],
        "instructions": [
            "Soak rice and dals with dried chili, then grind coarsely with salt.",
            "Mix in chopped onion and curry leaves; spread thickly on a griddle and cook both sides.",
        ],
    },
    "Ven Pongal": {
        "ingredients": ["Rice", "Yellow Moong Dal", "Black Pepper", "Cumin", "Ginger", "Cashews", "Ghee"],
        "instructions": [
            "Dry-roast moong dal, then cook it with rice and water until soft and creamy.",
            "Temper pepper, cumin, ginger, and cashews in ghee; stir into the pongal.",
        ],
    },
    "Sweet Pongal": {
        "ingredients": ["Rice", "Yellow Moong Dal", "Jaggery", "Cardamom", "Cashews", "Raisins", "Ghee"],
        "instructions": [
            "Cook rice and moong dal together until very soft.",
            "Melt jaggery with a little water, combine with the rice, and finish with cardamom and ghee-fried nuts.",
        ],
    },
    "Kootu": {
        "ingredients": ["Chana Dal", "Bottle Gourd", "Coconut", "Cumin", "Green Chili", "Mustard Seeds", "Curry Leaves"],
        "instructions": [
            "Cook chana dal and diced bottle gourd until tender.",
            "Blend coconut, cumin, and chili; simmer with the dal, then add a mustard seed and curry leaf tempering.",
        ],
    },
    "Avial": {
        "ingredients": ["Carrot", "Drumstick", "Green Beans", "Plantain", "Coconut", "Yogurt", "Curry Leaves"],
        "instructions": [
            "Cut vegetables into strips and cook with a little water, turmeric, and salt until just tender.",
            "Fold in crushed coconut and green chili, then finish with yogurt and coconut oil.",
        ],
    },
    "Beans Poriyal": {
        "ingredients": ["Green Beans", "Grated Coconut", "Mustard Seeds", "Urad Dal", "Curry Leaves", "Green Chili", "Turmeric"],
        "instructions": [
            "Chop beans and steam or saute until tender-crisp.",
            "Temper mustard seeds, urad dal, curry leaves, and chili; toss with beans, turmeric, and coconut.",
        ],
    },
    "Paruppu Usili": {
        "ingredients": ["Green Beans", "Toor Dal", "Chana Dal", "Dried Red Chili", "Mustard Seeds", "Curry Leaves", "Turmeric"],
        "instructions": [
            "Soak dals with dried chili, grind coarsely, and steam the mixture until firm; crumble it.",
            "Cook chopped beans until tender, then saute with the dal crumble and a mustard seed tempering.",
        ],
    },
    "Kozhukattai": {
        "ingredients": ["Rice Flour", "Grated Coconut", "Jaggery", "Cardamom", "Sesame Seeds", "Water"],
        "instructions": [
            "Cook jaggery with coconut, sesame, and cardamom until the filling is sticky; cool.",
            "Make a soft rice flour dough with hot water, fill and shape dumplings, then steam until glossy.",
        ],
    },
    "Kothu Parotta": {
        "ingredients": ["Parotta", "Egg", "Onion", "Tomato", "Green Chili", "Curry Leaves", "Salna"],
        "instructions": [
            "Shred cooked parotta into bite-sized pieces and saute onion, chili, and curry leaves.",
            "Add tomato, egg, and parotta; chop and toss on the pan with salna until hot.",
        ],
    },
    "Chettinad Egg Curry": {
        "ingredients": ["Egg", "Onion", "Tomato", "Coconut", "Fennel Seeds", "Black Pepper", "Curry Leaves"],
        "instructions": [
            "Boil and peel eggs; toast coconut, fennel, and pepper, then grind to a paste.",
            "Cook onion and tomato with curry leaves, add the paste and water, then simmer eggs in the sauce.",
        ],
    },
    "Erissery": {
        "ingredients": ["Pumpkin", "Black-Eyed Peas", "Coconut", "Cumin", "Dried Red Chili", "Mustard Seeds", "Curry Leaves"],
        "instructions": [
            "Cook soaked black-eyed peas and pumpkin with turmeric until tender.",
            "Add a ground coconut-cumin paste and simmer; finish with toasted coconut and mustard seeds.",
        ],
    },
    "Olan": {
        "ingredients": ["Ash Gourd", "Black-Eyed Peas", "Coconut Milk", "Green Chili", "Curry Leaves", "Coconut Oil", "Salt"],
        "instructions": [
            "Cook ash gourd and soaked black-eyed peas with green chili and a little water until tender.",
            "Add coconut milk and salt, warm gently without boiling, and finish with curry leaves and coconut oil.",
        ],
    },
    "Cabbage Thoran": {
        "ingredients": ["Cabbage", "Grated Coconut", "Mustard Seeds", "Cumin", "Green Chili", "Curry Leaves", "Turmeric"],
        "instructions": [
            "Shred cabbage and mix with coconut, cumin, chili, turmeric, and salt.",
            "Temper mustard seeds and curry leaves, add the cabbage, and cook covered until tender.",
        ],
    },
    "Malabar Parotta": {
        "ingredients": ["All-Purpose Flour", "Egg", "Milk", "Oil", "Sugar", "Salt", "Water"],
        "instructions": [
            "Knead flour, egg, milk, sugar, salt, and water into a soft elastic dough; rest with oil.",
            "Stretch and fold dough into layered coils, roll flat, and pan-cook until golden on both sides.",
        ],
    },
    "Nadan Chicken Curry": {
        "ingredients": ["Chicken", "Coconut Milk", "Onion", "Tomato", "Ginger", "Garlic", "Curry Leaves"],
        "instructions": [
            "Cook onion, ginger, garlic, and curry leaves until golden; add chicken and brown lightly.",
            "Add tomato, spices, and thin coconut milk; simmer until chicken is cooked, then finish with thick coconut milk.",
        ],
    },
    "Beef Ularthiyathu": {
        "ingredients": ["Beef", "Onion", "Shallot", "Black Pepper", "Coconut Slices", "Curry Leaves", "Coconut Oil"],
        "instructions": [
            "Pressure-cook beef with ginger, garlic, pepper, and salt until tender.",
            "Slow-fry with onion, shallot, coconut slices, and curry leaves in coconut oil until browned and dry.",
        ],
    },
    "Handvo": {
        "ingredients": ["Rice", "Toor Dal", "Bottle Gourd", "Yogurt", "Sesame Seeds", "Mustard Seeds", "Eno Fruit Salt"],
        "instructions": [
            "Soak and grind rice and dal; ferment with yogurt, then mix in grated bottle gourd and spices.",
            "Fold in fruit salt, top with sesame and mustard seeds, and bake until golden and cooked through.",
        ],
    },
    "Muthiya": {
        "ingredients": ["Fenugreek Leaves", "Whole Wheat Flour", "Gram Flour", "Yogurt", "Sesame Seeds", "Mustard Seeds", "Curry Leaves"],
        "instructions": [
            "Mix chopped fenugreek with flours, yogurt, spices, and water into a soft dough; shape into logs.",
            "Steam until firm, slice, then saute with sesame, mustard seeds, and curry leaves.",
        ],
    },
    "Dal Dhokli": {
        "ingredients": ["Toor Dal", "Whole Wheat Flour", "Peanuts", "Tomato", "Jaggery", "Tamarind", "Cumin"],
        "instructions": [
            "Cook toor dal with tomato, peanuts, turmeric, jaggery, and tamarind until soft.",
            "Roll spiced wheat dough thin, cut into diamonds, and simmer in the dal until cooked.",
        ],
    },
    "Gujarati Khichu": {
        "ingredients": ["Rice Flour", "Cumin", "Green Chili", "Carom Seeds", "Papad Kharo", "Water", "Oil"],
        "instructions": [
            "Bring water, cumin, chili, carom seeds, salt, and papad kharo to a boil.",
            "Stir in rice flour gradually and cook, stirring, until a smooth thick dough forms; serve warm with oil.",
        ],
    },
    "Patra": {
        "ingredients": ["Colocasia Leaves", "Gram Flour", "Tamarind", "Jaggery", "Sesame Seeds", "Cumin", "Green Chili"],
        "instructions": [
            "Mix gram flour with tamarind, jaggery, spices, and water into a spreadable paste.",
            "Layer paste on colocasia leaves, roll tightly, steam until firm, slice, and pan-fry with sesame.",
        ],
    },
    "Puran Poli": {
        "ingredients": ["Whole Wheat Flour", "Chana Dal", "Jaggery", "Cardamom", "Nutmeg", "Ghee", "Water"],
        "instructions": [
            "Cook chana dal until soft, drain well, and mash with jaggery, cardamom, and nutmeg.",
            "Wrap portions in a soft wheat dough, roll gently, and cook on a griddle with ghee.",
        ],
    },
    "Sabudana Khichdi": {
        "ingredients": ["Sabudana", "Potato", "Peanuts", "Cumin", "Green Chili", "Lemon", "Cilantro"],
        "instructions": [
            "Rinse and soak sabudana until pearls are soft but separate; crush roasted peanuts.",
            "Cook cumin, potato, and chili; add sabudana and peanuts and toss until translucent, then add lemon.",
        ],
    },
    "Thalipeeth": {
        "ingredients": ["Jowar Flour", "Whole Wheat Flour", "Chickpea Flour", "Onion", "Cilantro", "Green Chili", "Sesame Seeds"],
        "instructions": [
            "Mix flours with chopped onion, cilantro, chili, sesame, spices, and water into a soft dough.",
            "Pat into a thin round on a greased pan and cook both sides until crisp and browned.",
        ],
    },
    "Bharli Vangi": {
        "ingredients": ["Baby Eggplant", "Peanuts", "Sesame Seeds", "Coconut", "Onion", "Tamarind", "Jaggery"],
        "instructions": [
            "Roast and grind peanuts, sesame, and coconut; mix with onion, tamarind, jaggery, and spices.",
            "Stuff slit baby eggplants, arrange in a pan with water, cover, and simmer until tender.",
        ],
    },
    "Zunka Bhakri": {
        "ingredients": ["Gram Flour", "Onion", "Green Chili", "Garlic", "Mustard Seeds", "Cilantro", "Jowar Flour"],
        "instructions": [
            "Cook mustard seeds, onion, chili, and garlic; add gram flour and roast while sprinkling water until crumbly.",
            "Mix jowar flour with water, pat into flatbreads, cook on a griddle, and serve with zunka.",
        ],
    },
    "Kothimbir Vadi": {
        "ingredients": ["Cilantro", "Gram Flour", "Rice Flour", "Sesame Seeds", "Green Chili", "Ginger", "Lemon"],
        "instructions": [
            "Mix chopped cilantro with flours, sesame, chili, ginger, lemon, spices, and water into a thick batter.",
            "Steam in a greased tray until set, cool and slice, then shallow-fry until crisp.",
        ],
    },
    "Amritsari Kulcha": {
        "ingredients": ["All-Purpose Flour", "Yogurt", "Potato", "Onion", "Cilantro", "Green Chili", "Butter"],
        "instructions": [
            "Make a yogurt-based flour dough and rest it; mix mashed potato with onion, cilantro, and chili.",
            "Fill dough portions, roll flat, and bake in a very hot oven or cook on a griddle; brush with butter.",
        ],
    },
    "Pindi Chana": {
        "ingredients": ["Chickpeas", "Tea Bags", "Anardana", "Cumin", "Coriander Seeds", "Ginger", "Ghee"],
        "instructions": [
            "Soak chickpeas and pressure-cook with tea bags until tender; discard the tea bags.",
            "Roast and grind spices, then saute with ginger in ghee; toss with chickpeas and cook until dry.",
        ],
    },
    "Moong Dal Chilla": {
        "ingredients": ["Yellow Moong Dal", "Ginger", "Green Chili", "Cumin", "Onion", "Cilantro", "Oil"],
        "instructions": [
            "Soak moong dal and blend with ginger, chili, cumin, salt, and water into a batter.",
            "Spread thinly on a hot oiled griddle, add onion and cilantro, and cook both sides.",
        ],
    },
    "Besan Chilla": {
        "ingredients": ["Gram Flour", "Onion", "Tomato", "Green Chili", "Cilantro", "Ajwain", "Water"],
        "instructions": [
            "Whisk gram flour with water, ajwain, salt, and chopped vegetables into a smooth batter.",
            "Pour a thin layer onto a hot greased griddle and cook both sides until golden.",
        ],
    },
    "Aloo Methi": {
        "ingredients": ["Potato", "Fenugreek Leaves", "Cumin", "Garlic", "Green Chili", "Turmeric", "Amchur"],
        "instructions": [
            "Cook cumin, garlic, and chili in oil; add cubed potato and turmeric and cover until nearly tender.",
            "Add chopped fenugreek leaves and amchur; cook uncovered until the potatoes are soft.",
        ],
    },
    "Dahi Aloo": {
        "ingredients": ["Potato", "Yogurt", "Cumin", "Ginger", "Coriander Powder", "Turmeric", "Cilantro"],
        "instructions": [
            "Boil and cube potatoes; whisk yogurt with coriander, turmeric, and a little water.",
            "Cook cumin and ginger, add potatoes and yogurt mixture, and simmer gently until thick.",
        ],
    },
    "Mushroom Masala": {
        "ingredients": ["Mushroom", "Onion", "Tomato", "Ginger", "Garlic", "Coriander Powder", "Garam Masala"],
        "instructions": [
            "Cook onion, ginger, and garlic until golden; add tomato and coriander powder and cook down.",
            "Add sliced mushrooms and simmer until tender; finish with garam masala.",
        ],
    },
    "Mushroom Pepper Fry": {
        "ingredients": ["Mushroom", "Onion", "Black Pepper", "Fennel Seeds", "Curry Leaves", "Garlic", "Coconut Oil"],
        "instructions": [
            "Crush black pepper and fennel; saute garlic, onion, and curry leaves in coconut oil.",
            "Add mushrooms and salt, then stir-fry until browned and coated in the pepper spice.",
        ],
    },
    "Kadai Mushroom": {
        "ingredients": ["Mushroom", "Bell Pepper", "Tomato", "Onion", "Coriander Seeds", "Ginger", "Kashmiri Chili"],
        "instructions": [
            "Toast and crush coriander seeds with Kashmiri chili; cook onion, ginger, and tomato.",
            "Add mushrooms and bell pepper with the spice mix and cook until tender but not soft.",
        ],
    },
    "Matar Mushroom": {
        "ingredients": ["Mushroom", "Peas", "Tomato", "Onion", "Ginger", "Cumin", "Garam Masala"],
        "instructions": [
            "Cook cumin, onion, and ginger, then add tomato and simmer into a thick masala.",
            "Add mushrooms, peas, and water; cover and cook until tender, then add garam masala.",
        ],
    },
    "Corn Palak": {
        "ingredients": ["Spinach", "Sweet Corn", "Onion", "Tomato", "Garlic", "Ginger", "Garam Masala"],
        "instructions": [
            "Blanch spinach and blend to a puree; cook onion, garlic, ginger, and tomato until soft.",
            "Add spinach, corn, and spices; simmer gently until the corn is tender.",
        ],
    },
    "Methi Malai Matar": {
        "ingredients": ["Fenugreek Leaves", "Peas", "Heavy Cream", "Onion", "Cashews", "Ginger", "Cardamom"],
        "instructions": [
            "Blend cooked onion and soaked cashews into a smooth paste; saute chopped fenugreek leaves.",
            "Add peas, cashew paste, cardamom, and water; simmer until tender, then stir in cream.",
        ],
    },
    "Lauki Kofta": {
        "ingredients": ["Bottle Gourd", "Gram Flour", "Tomato", "Onion", "Ginger", "Cumin", "Garam Masala"],
        "instructions": [
            "Grate and squeeze bottle gourd, mix with gram flour and spices, shape into balls, and fry.",
            "Cook onion, tomato, ginger, and cumin into a gravy; add koftas shortly before serving.",
        ],
    },
    "Kashmiri Haak": {
        "ingredients": ["Collard Greens", "Mustard Oil", "Dried Red Chili", "Asafoetida", "Fennel Seeds", "Ginger", "Salt"],
        "instructions": [
            "Heat mustard oil and add asafoetida, dried chili, fennel, and sliced ginger.",
            "Add washed greens and salt with a little water; cover and simmer until tender.",
        ],
    },
    "Kashmiri Nadru Yakhni": {
        "ingredients": ["Lotus Root", "Yogurt", "Fennel Powder", "Dry Ginger Powder", "Cardamom", "Cumin", "Mustard Oil"],
        "instructions": [
            "Boil sliced lotus root until tender and drain.",
            "Whisk yogurt with fennel and ginger powders; simmer with whole spices and lotus root until creamy.",
        ],
    },
    "Kashmiri Rogan Josh (Vegetarian)": {
        "ingredients": ["Mushroom", "Yogurt", "Kashmiri Chili", "Fennel Powder", "Dry Ginger Powder", "Cardamom", "Ghee"],
        "instructions": [
            "Brown mushrooms lightly in ghee with cardamom and Kashmiri chili.",
            "Stir in whisked yogurt, fennel, ginger powder, and water; simmer until the sauce thickens.",
        ],
    },
    "Kashmiri Modur Pulao": {
        "ingredients": ["Basmati Rice", "Milk", "Saffron", "Sugar", "Almonds", "Raisins", "Cinnamon"],
        "instructions": [
            "Soak saffron in warm milk; rinse and soak basmati rice.",
            "Cook rice with cinnamon, sugar, saffron milk, almonds, raisins, and water until fragrant and fluffy.",
        ],
    },
    "Sindhi Sai Bhaji": {
        "ingredients": ["Spinach", "Chana Dal", "Dill", "Tomato", "Onion", "Garlic", "Green Chili"],
        "instructions": [
            "Pressure-cook spinach, dill, chana dal, tomato, onion, garlic, and chili with water until soft.",
            "Mash lightly, season, and simmer until thick; serve with rice.",
        ],
    },
    "Sindhi Kadhi": {
        "ingredients": ["Gram Flour", "Tamarind", "Drumstick", "Potato", "Carrot", "Tomato", "Curry Leaves"],
        "instructions": [
            "Roast gram flour in oil until fragrant; slowly whisk in water to make a smooth gravy.",
            "Add tamarind, tomato, and vegetables; simmer until tender and finish with curry leaves.",
        ],
    },
    "Sindhi Koki": {
        "ingredients": ["Whole Wheat Flour", "Onion", "Cilantro", "Green Chili", "Cumin", "Anardana", "Ghee"],
        "instructions": [
            "Mix flour with finely chopped onion, cilantro, chili, cumin, anardana, salt, and ghee.",
            "Knead with little water, roll thick, and cook slowly on a griddle until crisp and cooked through.",
        ],
    },
    "Andhra Gongura Pachadi": {
        "ingredients": ["Gongura Leaves", "Dried Red Chili", "Garlic", "Cumin", "Mustard Seeds", "Fenugreek Seeds", "Sesame Oil"],
        "instructions": [
            "Wash and dry gongura leaves, then saute until wilted and set aside.",
            "Toast chilies, cumin, and fenugreek; grind with the leaves and garlic, then finish with mustard tempering.",
        ],
    },
    "Andhra Chicken Curry": {
        "ingredients": ["Chicken", "Onion", "Tomato", "Curry Leaves", "Coriander Seeds", "Dried Red Chili", "Coconut"],
        "instructions": [
            "Toast coriander, red chili, and coconut, then grind to a coarse masala.",
            "Cook onion and curry leaves, add chicken and tomato, then simmer with the masala until tender.",
        ],
    },
    "Gutti Vankaya": {
        "ingredients": ["Baby Eggplant", "Peanuts", "Sesame Seeds", "Coconut", "Onion", "Tamarind", "Coriander Seeds"],
        "instructions": [
            "Roast peanuts, sesame, coconut, and coriander; grind with onion and tamarind into a paste.",
            "Stuff slit eggplants, then cover and simmer with water and remaining paste until soft.",
        ],
    },
    "Andhra Pulihora": {
        "ingredients": ["Rice", "Tamarind", "Peanuts", "Mustard Seeds", "Turmeric", "Curry Leaves", "Dried Red Chili"],
        "instructions": [
            "Cook rice and cool it so the grains remain separate; simmer tamarind pulp with turmeric and salt.",
            "Temper mustard seeds, peanuts, chili, and curry leaves; mix with tamarind paste and rice.",
        ],
    },
    "Andhra Gongura Mutton": {
        "ingredients": ["Mutton", "Gongura Leaves", "Onion", "Ginger", "Garlic", "Green Chili", "Garam Masala"],
        "instructions": [
            "Pressure-cook mutton with ginger, garlic, onion, and spices until tender.",
            "Saute gongura leaves until soft, stir into the mutton, and simmer until the gravy is thick.",
        ],
    },
    "Egg Bhurji": {
        "ingredients": ["Egg", "Onion", "Tomato", "Green Chili", "Turmeric", "Cumin", "Cilantro"],
        "instructions": [
            "Cook cumin, onion, and chili until soft; add tomato and turmeric and cook down.",
            "Pour in beaten eggs and stir gently until just set; finish with cilantro.",
        ],
    },
    "Egg Roast": {
        "ingredients": ["Egg", "Onion", "Tomato", "Black Pepper", "Fennel Seeds", "Curry Leaves", "Coconut Oil"],
        "instructions": [
            "Boil and peel eggs; saute onion, fennel, and curry leaves in coconut oil.",
            "Add tomato and pepper, cook to a thick masala, then add eggs and coat well.",
        ],
    },
    "Anda Curry": {
        "ingredients": ["Egg", "Onion", "Tomato", "Ginger", "Garlic", "Cumin", "Coriander Powder"],
        "instructions": [
            "Boil and peel eggs; cook cumin, onion, ginger, and garlic until golden.",
            "Add tomato and coriander powder, simmer into a gravy, then add eggs and cook briefly.",
        ],
    },
    "Chicken Saagwala": {
        "ingredients": ["Chicken", "Spinach", "Onion", "Tomato", "Ginger", "Garlic", "Garam Masala"],
        "instructions": [
            "Blanch spinach and blend; brown chicken pieces and set aside.",
            "Cook onion, ginger, garlic, and tomato, add spinach and chicken, then simmer until cooked.",
        ],
    },
    "Chicken Do Pyaza": {
        "ingredients": ["Chicken", "Onion", "Tomato", "Yogurt", "Ginger", "Garlic", "Coriander Powder"],
        "instructions": [
            "Brown chicken and set aside; cook half the onions with ginger and garlic until soft.",
            "Add tomato, spices, yogurt, chicken, and remaining onion; cover and simmer until tender.",
        ],
    },
    "Chicken Dhansak": {
        "ingredients": ["Chicken", "Toor Dal", "Masoor Dal", "Pumpkin", "Tomato", "Fenugreek Leaves", "Dhansak Masala"],
        "instructions": [
            "Cook lentils and pumpkin until soft, then blend or mash coarsely.",
            "Brown chicken with onion and dhansak masala; add tomato and lentils and simmer until cooked.",
        ],
    },
    "Chicken Kolhapuri": {
        "ingredients": ["Chicken", "Onion", "Tomato", "Dried Red Chili", "Coconut", "Sesame Seeds", "Garam Masala"],
        "instructions": [
            "Toast dried chili, coconut, and sesame, then grind into a spicy paste.",
            "Cook onion and tomato, add chicken and the paste, then simmer until tender and richly coated.",
        ],
    },
    "Mutton Sukka": {
        "ingredients": ["Mutton", "Coconut", "Onion", "Black Pepper", "Fennel Seeds", "Curry Leaves", "Coconut Oil"],
        "instructions": [
            "Pressure-cook mutton with salt and turmeric until tender; reserve a little cooking liquid.",
            "Toast coconut, pepper, and fennel; cook with onion and curry leaves, then toss in mutton until dry.",
        ],
    },
    "Mutton Yakhni Pulao": {
        "ingredients": ["Mutton", "Basmati Rice", "Yogurt", "Fennel Seeds", "Cardamom", "Cinnamon", "Onion"],
        "instructions": [
            "Simmer mutton with whole spices and onion until tender; strain and reserve the broth.",
            "Cook soaked rice with yogurt, mutton, and measured broth until fluffy and aromatic.",
        ],
    },
    "Keema Pav": {
        "ingredients": ["Ground Beef", "Pav Bread", "Onion", "Tomato", "Ginger", "Garlic", "Peas"],
        "instructions": [
            "Cook onion, ginger, and garlic, then brown ground beef thoroughly.",
            "Add tomato, peas, and spices; simmer until thick and serve with butter-toasted pav.",
        ],
    },
    "Chicken Cafreal": {
        "ingredients": ["Chicken", "Cilantro", "Mint", "Green Chili", "Garlic", "Ginger", "Lemon"],
        "instructions": [
            "Blend cilantro, mint, chili, garlic, ginger, lemon, and spices into a green marinade.",
            "Coat chicken and marinate, then pan-roast or grill until browned and cooked through.",
        ],
    },
    "Goan Xacuti": {
        "ingredients": ["Chicken", "Coconut", "Poppy Seeds", "Dried Red Chili", "Coriander Seeds", "Onion", "Tamarind"],
        "instructions": [
            "Toast coconut, poppy seeds, chilies, and coriander; grind with water into a paste.",
            "Cook onion and chicken, add the spice paste and tamarind, then simmer until tender.",
        ],
    },
    "Goan Pork Vindaloo": {
        "ingredients": ["Pork", "Vinegar", "Dried Red Chili", "Garlic", "Ginger", "Cumin", "Onion"],
        "instructions": [
            "Blend vinegar, dried chili, garlic, ginger, cumin, and spices; marinate pork in the paste.",
            "Brown onion and pork, add water, and simmer slowly until tender and the sauce is rich.",
        ],
    },
    "Prawn Balchao": {
        "ingredients": ["Prawns", "Vinegar", "Dried Red Chili", "Garlic", "Ginger", "Onion", "Tomato"],
        "instructions": [
            "Marinate prawns briefly with salt; blend chili, vinegar, garlic, and ginger.",
            "Cook onion and tomato, add the spice paste and prawns, and simmer until cooked and tangy.",
        ],
    },
    "Fish Moilee": {
        "ingredients": ["Fish", "Coconut Milk", "Onion", "Green Chili", "Ginger", "Turmeric", "Curry Leaves"],
        "instructions": [
            "Lightly sear fish pieces and set aside; cook onion, ginger, chili, and turmeric.",
            "Add thin coconut milk and simmer, return fish to cook gently, then finish with thick coconut milk.",
        ],
    },
    "Prawn Ghee Roast": {
        "ingredients": ["Prawns", "Ghee", "Dried Red Chili", "Garlic", "Tamarind", "Cumin", "Curry Leaves"],
        "instructions": [
            "Soak dried chilies and grind with garlic, cumin, tamarind, and a splash of water.",
            "Cook the masala in ghee until aromatic, add prawns, and toss until just cooked.",
        ],
    },
    "Masala Fish Fry": {
        "ingredients": ["Fish", "Chili Powder", "Turmeric", "Ginger", "Garlic", "Lemon", "Rice Flour"],
        "instructions": [
            "Mix chili, turmeric, ginger, garlic, lemon, and salt into a paste and coat fish.",
            "Dust lightly with rice flour and shallow-fry until crisp outside and cooked through.",
        ],
    },
    "Amritsari Fish": {
        "ingredients": ["Firm White Fish", "Gram Flour", "Yogurt", "Ajwain", "Ginger", "Garlic", "Lemon"],
        "instructions": [
            "Cut fish into pieces and coat with yogurt, lemon, ginger, garlic, ajwain, and salt.",
            "Dust with gram flour and fry in batches until crisp and the fish flakes easily.",
        ],
    },
    "Tandoori Gobi": {
        "ingredients": ["Cauliflower", "Yogurt", "Tandoori Masala", "Ginger", "Garlic", "Lemon", "Gram Flour"],
        "instructions": [
            "Blanch cauliflower briefly and drain; mix yogurt with tandoori masala, ginger, garlic, and lemon.",
            "Coat florets, dust with gram flour, and roast at high heat until charred and tender.",
        ],
    },
    "Paneer Tikka": {
        "ingredients": ["Paneer", "Yogurt", "Bell Pepper", "Onion", "Ginger", "Garlic", "Tandoori Masala"],
        "instructions": [
            "Mix yogurt, ginger, garlic, and tandoori masala; coat paneer and vegetable chunks.",
            "Thread onto skewers and grill or roast, turning until lightly charred.",
        ],
    },
    "Achari Paneer": {
        "ingredients": ["Paneer", "Yogurt", "Mustard Seeds", "Fennel Seeds", "Fenugreek Seeds", "Tomato", "Kashmiri Chili"],
        "instructions": [
            "Toast mustard, fennel, and fenugreek seeds, then crush coarsely.",
            "Cook tomato with chili and the spice mix; stir in yogurt and paneer and simmer gently.",
        ],
    },
    "Paneer Lababdar": {
        "ingredients": ["Paneer", "Tomato", "Onion", "Cashews", "Butter", "Heavy Cream", "Kasuri Methi"],
        "instructions": [
            "Cook tomato, onion, and cashews until soft, then blend into a smooth sauce.",
            "Simmer the sauce with butter and spices, add paneer and cream, and finish with kasuri methi.",
        ],
    },
    "Paneer Do Pyaza": {
        "ingredients": ["Paneer", "Onion", "Tomato", "Bell Pepper", "Ginger", "Coriander Powder", "Garam Masala"],
        "instructions": [
            "Cook half the onion with ginger and tomato until soft; blend into a gravy.",
            "Add paneer, bell pepper, remaining onion, and spices; simmer until the vegetables are tender.",
        ],
    },
    "Paneer Jalfrezi": {
        "ingredients": ["Paneer", "Bell Pepper", "Onion", "Tomato", "Ginger", "Cumin", "Kashmiri Chili"],
        "instructions": [
            "Stir-fry onion, bell pepper, ginger, and cumin over high heat until crisp-tender.",
            "Add tomato, chili, and paneer; toss until hot and coated in the masala.",
        ],
    },
    "Corn Cheese Balls": {
        "ingredients": ["Sweet Corn", "Cheddar Cheese", "Potato", "Breadcrumbs", "Green Chili", "Cilantro", "Corn Flour"],
        "instructions": [
            "Mash potato with corn, cheese, chili, cilantro, and salt; shape into balls.",
            "Coat with corn flour slurry and breadcrumbs, then fry until golden and crisp.",
        ],
    },
    "Masala Papad": {
        "ingredients": ["Papad", "Onion", "Tomato", "Cilantro", "Green Chili", "Lemon", "Chaat Masala"],
        "instructions": [
            "Roast or fry papad until crisp.",
            "Top just before serving with finely chopped onion, tomato, chili, cilantro, lemon, and chaat masala.",
        ],
    },
    "Dabeli": {
        "ingredients": ["Pav Bread", "Potato", "Dabeli Masala", "Peanuts", "Pomegranate", "Tamarind Chutney", "Garlic Chutney"],
        "instructions": [
            "Mash cooked potato with dabeli masala and tamarind chutney; mix in roasted peanuts.",
            "Fill butter-toasted pav with the potato mixture, chutneys, pomegranate, and sev.",
        ],
    },
    "Ragda Pattice": {
        "ingredients": ["White Peas", "Potato", "Tamarind Chutney", "Cilantro Chutney", "Onion", "Sev", "Chaat Masala"],
        "instructions": [
            "Soak and cook white peas until soft, then simmer with spices into a thick ragda.",
            "Pan-fry potato patties until crisp, spoon ragda over them, and top with chutneys, onion, and sev.",
        ],
    },
    "Sev Puri": {
        "ingredients": ["Papdi", "Potato", "Onion", "Tamarind Chutney", "Cilantro Chutney", "Sev", "Chaat Masala"],
        "instructions": [
            "Arrange papdi and top each with a little diced potato and onion.",
            "Drizzle with both chutneys, sprinkle chaat masala, and finish with sev just before serving.",
        ],
    },
    "Dabeli Masala Corn": {
        "ingredients": ["Sweet Corn", "Butter", "Dabeli Masala", "Lemon", "Cilantro", "Sev", "Peanuts"],
        "instructions": [
            "Saute sweet corn in butter with dabeli masala until hot.",
            "Add lemon and cilantro, then top with peanuts and sev to serve.",
        ],
    },
    "Chana Dal Fry": {
        "ingredients": ["Chana Dal", "Onion", "Tomato", "Garlic", "Cumin", "Turmeric", "Ghee"],
        "instructions": [
            "Rinse and pressure-cook chana dal with turmeric until tender but still holding shape.",
            "Cook cumin, garlic, onion, and tomato in ghee; stir into the dal and simmer briefly.",
        ],
    },
    "Japanese Chicken Teriyaki": {
        "ingredients": ["Chicken", "Soy Sauce", "Mirin", "Sugar", "Ginger", "Garlic", "Rice"],
        "instructions": [
            "Cook chicken in a hot pan until browned and cooked through.",
            "Simmer soy sauce, mirin, sugar, ginger, and garlic into a glaze; coat chicken and serve with rice.",
        ],
    },
    "Miso Soup": {
        "ingredients": ["Miso Paste", "Dashi", "Tofu", "Wakame", "Green Onion"],
        "instructions": [
            "Warm dashi and add cubed tofu and wakame until heated through.",
            "Dissolve miso paste in a little broth, stir it into the pot without boiling, and top with green onion.",
        ],
    },
    "Vegetable Sushi Rolls": {
        "ingredients": ["Sushi Rice", "Nori", "Cucumber", "Avocado", "Rice Vinegar", "Sugar", "Soy Sauce"],
        "instructions": [
            "Season cooked sushi rice with rice vinegar and sugar, then cool.",
            "Spread rice over nori, add cucumber and avocado, roll tightly, slice, and serve with soy sauce.",
        ],
    },
    "Bibimbap": {
        "ingredients": ["Rice", "Spinach", "Carrot", "Mushroom", "Egg", "Gochujang", "Sesame Oil"],
        "instructions": [
            "Cook rice and prepare vegetables separately by sauteing or blanching each until tender.",
            "Arrange over rice, top with a fried egg, and serve with gochujang and sesame oil.",
        ],
    },
    "Kimchi Fried Rice": {
        "ingredients": ["Rice", "Kimchi", "Egg", "Green Onion", "Soy Sauce", "Sesame Oil", "Nori"],
        "instructions": [
            "Chop kimchi and stir-fry it with green onion until fragrant.",
            "Add cooked rice, soy sauce, and sesame oil; fry until hot and serve with egg and nori.",
        ],
    },
    "Pad Thai": {
        "ingredients": ["Rice Noodles", "Shrimp", "Egg", "Bean Sprouts", "Peanuts", "Tamarind", "Fish Sauce"],
        "instructions": [
            "Soak rice noodles until pliable; mix tamarind with fish sauce and a little sugar.",
            "Stir-fry shrimp and egg, add noodles and sauce, toss with bean sprouts, and top with peanuts.",
        ],
    },
    "Thai Green Curry": {
        "ingredients": ["Chicken", "Green Curry Paste", "Coconut Milk", "Thai Eggplant", "Basil", "Fish Sauce", "Rice"],
        "instructions": [
            "Fry green curry paste briefly, then stir in coconut milk and bring to a gentle simmer.",
            "Add chicken and eggplant; cook through, season with fish sauce, and finish with basil.",
        ],
    },
    "Vietnamese Pho": {
        "ingredients": ["Rice Noodles", "Beef", "Beef Stock", "Onion", "Ginger", "Star Anise", "Cilantro"],
        "instructions": [
            "Simmer beef stock with charred onion, ginger, and star anise, then strain and season.",
            "Cook rice noodles, arrange with thin beef slices, pour over hot broth, and garnish with cilantro.",
        ],
    },
    "Hummus": {
        "ingredients": ["Chickpeas", "Tahini", "Lemon", "Garlic", "Olive Oil", "Cumin"],
        "instructions": [
            "Blend chickpeas with tahini, lemon juice, garlic, cumin, and a little cold water.",
            "Adjust salt and texture, then serve with olive oil drizzled over the top.",
        ],
    },
    "Falafel": {
        "ingredients": ["Dried Chickpeas", "Parsley", "Cilantro", "Onion", "Garlic", "Cumin", "Coriander"],
        "instructions": [
            "Soak dried chickpeas overnight, drain, and pulse with herbs, onion, garlic, and spices.",
            "Shape into small patties and fry until crisp and cooked through.",
        ],
    },
    "Shakshuka": {
        "ingredients": ["Egg", "Tomato", "Bell Pepper", "Onion", "Garlic", "Cumin", "Paprika"],
        "instructions": [
            "Cook onion and bell pepper until soft; add garlic, cumin, paprika, and chopped tomatoes.",
            "Simmer until thick, make wells, add eggs, cover, and cook until the whites are set.",
        ],
    },
    "Tabbouleh": {
        "ingredients": ["Bulgur Wheat", "Parsley", "Mint", "Tomato", "Cucumber", "Lemon", "Olive Oil"],
        "instructions": [
            "Soak bulgur until tender, then drain well; finely chop parsley, mint, tomato, and cucumber.",
            "Toss with lemon juice, olive oil, salt, and the bulgur; chill briefly before serving.",
        ],
    },
    "Greek Chicken Souvlaki": {
        "ingredients": ["Chicken", "Lemon", "Olive Oil", "Oregano", "Garlic", "Yogurt", "Pita Bread"],
        "instructions": [
            "Marinate chicken cubes with lemon, olive oil, oregano, garlic, and salt.",
            "Thread onto skewers and grill until cooked through; serve with pita and yogurt sauce.",
        ],
    },
    "Greek Moussaka": {
        "ingredients": ["Eggplant", "Ground Beef", "Tomato", "Onion", "Potato", "Milk", "Parmesan"],
        "instructions": [
            "Roast eggplant and potato slices; cook ground beef with onion and tomato into a thick sauce.",
            "Layer vegetables and meat sauce, cover with a milk-based white sauce and Parmesan, then bake until golden.",
        ],
    },
    "Spanish Tortilla": {
        "ingredients": ["Potato", "Egg", "Onion", "Olive Oil", "Salt"],
        "instructions": [
            "Slowly cook thin potato and onion slices in olive oil until tender, then drain.",
            "Mix with beaten eggs and cook in a skillet until set, carefully turning to brown the other side.",
        ],
    },
    "Ratatouille": {
        "ingredients": ["Eggplant", "Zucchini", "Bell Pepper", "Tomato", "Onion", "Garlic", "Olive Oil"],
        "instructions": [
            "Slice vegetables into even pieces; cook onion and garlic in olive oil until soft.",
            "Layer vegetables in a baking dish, season, drizzle with oil, and bake until tender.",
        ],
    },
    "French Crepes": {
        "ingredients": ["All-Purpose Flour", "Milk", "Egg", "Butter", "Sugar", "Salt"],
        "instructions": [
            "Whisk flour, milk, egg, melted butter, sugar, and salt into a smooth thin batter; rest briefly.",
            "Pour a small amount into a lightly buttered pan, swirl thinly, and cook both sides.",
        ],
    },
    "Italian Lasagna": {
        "ingredients": ["Lasagna Sheets", "Ground Beef", "Tomato Sauce", "Ricotta", "Mozzarella", "Parmesan", "Onion"],
        "instructions": [
            "Cook ground beef with onion and tomato sauce; prepare ricotta with seasoning.",
            "Layer sauce, pasta sheets, ricotta, and mozzarella; top with Parmesan and bake until bubbling.",
        ],
    },
    "Mexican Enchiladas": {
        "ingredients": ["Corn Tortilla", "Chicken", "Tomato Sauce", "Cheddar Cheese", "Onion", "Cumin", "Chili Powder"],
        "instructions": [
            "Cook shredded chicken with onion, cumin, and chili powder.",
            "Fill tortillas, roll into a baking dish, cover with tomato sauce and cheese, and bake until hot.",
        ],
    },
    "Black Bean Burrito Bowl": {
        "ingredients": ["Rice", "Black Beans", "Corn", "Avocado", "Tomato", "Lime", "Cilantro"],
        "instructions": [
            "Cook rice and warm black beans with cumin and salt; prepare corn and chopped vegetables.",
            "Serve in bowls with avocado, tomato, lime juice, and cilantro.",
        ],
    },
    "Fish Tacos": {
        "ingredients": ["White Fish", "Corn Tortilla", "Cabbage", "Lime", "Yogurt", "Cumin", "Paprika"],
        "instructions": [
            "Season fish with cumin, paprika, and salt; pan-cook until flaky.",
            "Serve in warm tortillas with shredded cabbage, lime, and a simple yogurt sauce.",
        ],
    },
    "Chili Con Carne": {
        "ingredients": ["Ground Beef", "Kidney Beans", "Tomato", "Onion", "Garlic", "Chili Powder", "Cumin"],
        "instructions": [
            "Brown ground beef with onion and garlic, then stir in chili powder and cumin.",
            "Add tomato and kidney beans; simmer until thick and season to taste.",
        ],
    },
    "Chinese Vegetable Dumplings": {
        "ingredients": ["Dumpling Wrappers", "Cabbage", "Mushroom", "Carrot", "Ginger", "Soy Sauce", "Sesame Oil"],
        "instructions": [
            "Finely chop vegetables and stir-fry with ginger, soy sauce, and sesame oil; cool completely.",
            "Fill wrappers, seal edges, and steam or pan-fry until the filling is hot and wrappers are cooked.",
        ],
    },
    "Mapo Tofu": {
        "ingredients": ["Tofu", "Ground Pork", "Doubanjiang", "Garlic", "Ginger", "Soy Sauce", "Spring Onion"],
        "instructions": [
            "Brown ground pork with garlic, ginger, and doubanjiang.",
            "Add tofu cubes, soy sauce, and a little stock; simmer gently and garnish with spring onion.",
        ],
    },
    "Japanese Ramen": {
        "ingredients": ["Ramen Noodles", "Chicken Stock", "Egg", "Mushroom", "Soy Sauce", "Ginger", "Green Onion"],
        "instructions": [
            "Simmer chicken stock with ginger, mushrooms, and soy sauce to make a flavorful broth.",
            "Cook noodles separately, place in bowls, pour over broth, and top with egg and green onion.",
        ],
    },
    "Greek Tzatziki": {
        "ingredients": ["Greek Yogurt", "Cucumber", "Garlic", "Lemon", "Dill", "Olive Oil", "Salt"],
        "instructions": [
            "Grate cucumber, squeeze out excess liquid, and mix with Greek yogurt and crushed garlic.",
            "Add lemon, dill, olive oil, and salt; chill before serving.",
        ],
    },
    "Turkish Menemen": {
        "ingredients": ["Egg", "Tomato", "Green Bell Pepper", "Onion", "Olive Oil", "Paprika", "Parsley"],
        "instructions": [
            "Cook onion and green pepper in olive oil until soft; add chopped tomato and paprika.",
            "When tomatoes are saucy, stir in eggs and cook gently until just set; garnish with parsley.",
        ],
    },
    "Brazilian Pao de Queijo": {
        "ingredients": ["Tapioca Flour", "Milk", "Oil", "Egg", "Parmesan", "Mozzarella", "Salt"],
        "instructions": [
            "Heat milk, oil, and salt until steaming, then pour over tapioca flour and mix.",
            "Cool slightly, knead in egg and cheeses, shape into balls, and bake until puffed and golden.",
        ],
    },
}


def _normalize_ingredient(ingredient):
    """Normalize ingredient capitalization, whitespace, and common plurals."""
    words = ingredient.strip().casefold().split()
    if not words:
        return ""

    word = words[-1]
    irregular_plurals = {
        "leaves": "leaf",
        "loaves": "loaf",
        "knives": "knife",
        "wives": "wife",
        "molasses": "molasses",
        "cookies": "cookie",
        "brownies": "brownie",
        "smoothies": "smoothie",
    }
    if word in irregular_plurals:
        words[-1] = irregular_plurals[word]
    elif word.endswith("ies"):
        words[-1] = word[:-3] + "y"
    elif word.endswith("oes"):
        words[-1] = word[:-2]
    elif word.endswith(("ches", "shes", "xes", "zes", "sses")):
        words[-1] = word[:-2]
    elif word.endswith("s") and not word.endswith(("ss", "us", "is")):
        words[-1] = word[:-1]

    return " ".join(words)


def compare(user_ingredients, recipes=RECIPES):
    """Return recipe matches for the GUI instead of printing to the terminal."""
    # Normalize whitespace, capitalization, and common singular/plural forms.
    user_ingredients = {
        _normalize_ingredient(ingredient)
        for ingredient in user_ingredients
        if _normalize_ingredient(ingredient)
    }

    results = []

    for recipe_name, recipe_data in recipes.items():
        recipe_ingredients = recipe_data["ingredients"]
        matched = [
            ingredient
            for ingredient in recipe_ingredients
            if _normalize_ingredient(ingredient) in user_ingredients
        ]
        missing = [
            ingredient
            for ingredient in recipe_ingredients
            if _normalize_ingredient(ingredient) not in user_ingredients
        ]

        # Only show recipes for which the user has at least one ingredient.
        if not matched:
            continue

        percentage = len(matched) / len(recipe_ingredients) * 100

        results.append({
            "name": recipe_name,
            "percentage": percentage,
            "matched": matched,
            "missing": missing,
            "instructions": recipe_data["instructions"],
        })

    # Best matches first.
    results.sort(key=lambda recipe: recipe["percentage"], reverse=True)
    return results


if __name__ == "__main__":
    user_ingredients = []

    print("Enter ingredients one at a time. Type 'stop' when finished.")
    while True:
        user = input("Ingredient: ").strip()
        if user.casefold() == "stop":
            break
        if user:
            user_ingredients.append(user)

    matches = compare(user_ingredients)

    if not matches:
        print("No matching recipes found.")
    else:
        for recipe in matches:
            print(f"\n{recipe['name']} - {recipe['percentage']:.0f}% match")
            print("You have: " + ", ".join(recipe["matched"]))
            if recipe["missing"]:
                print("Missing: " + ", ".join(recipe["missing"]))
            else:
                print("Cooking Instructions:")
                for number, step in enumerate(recipe["instructions"], start=1):
                    print(f"{number}. {step}")
