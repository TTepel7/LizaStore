<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    use HasFactory;
    public function media(){
        return $this->belongsToMany(Category::class, 'media_categories');
    }
    protected $fillable=['name'];
}
