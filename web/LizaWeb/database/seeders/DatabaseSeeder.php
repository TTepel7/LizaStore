<?php

namespace Database\Seeders;

use App\Models\Category;
use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // \App\Models\User::factory(10)->create();
        Category::create([
            'name' => 'Авиа'
        ]);
        Category::create([
            'name' => 'Автомобили'
        ]);
        Category::create([
            'name' => 'БПЛА'
        ]);
        Category::create([
            'name' => 'Водолаз'
        ]);
        Category::create([
            'name' => 'Кинолог'
        ]);
        Category::create([
            'name' => 'Кони'
        ]);
        Category::create([
            'name' => 'Объятия'
        ]);
        Category::create([
            'name' => 'Шерп'
        ]);
        Category::create([
            'name' => 'День'
        ]);
        Category::create([
            'name' => 'Ночь'
        ]);
        Category::create([
            'name' => 'Рассвет/закат'
        ]);
        Category::create([
            'name' => 'Зима'
        ]);
        Category::create([
            'name' => 'Весна'
        ]);
        Category::create([
            'name' => 'Лето'
        ]);
        Category::create([
            'name' => 'Осень'
        ]);
        Category::create([
            'name' => 'Лес'
        ]);
        Category::create([
            'name' => 'Город'
        ]);

        User::create([
           'name'=>'Анастасия',
           'email'=>'Liza@alert.ru',
           'password'=>Hash::make('qwerty52')
        ]);

    }
}
