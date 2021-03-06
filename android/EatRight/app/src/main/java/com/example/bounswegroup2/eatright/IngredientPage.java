package com.example.bounswegroup2.eatright;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ListView;

import com.example.bounswegroup2.Models.Ingredient;

import java.util.ArrayList;

/**
 * The type Ingredient page.
 */
public class IngredientPage extends AppCompatActivity {
private ArrayList<Ingredient> ingredients = new ArrayList<Ingredient>();
    /**
     * The List view.
     */
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ingredient_page);
       ingredients = (ArrayList<Ingredient>) getIntent().getExtras().get("ingredients");
        listView = (ListView) findViewById(R.id.ingr_list);
        //View header = getLayoutInflater().inflate(R.diet_raw_layout.ingr_list_header,null);

        //listView.addHeaderView(header);
        IngredientAdapter ingr = new IngredientAdapter(IngredientPage.this,ingredients);
        listView.setAdapter(ingr);
    }

    }

