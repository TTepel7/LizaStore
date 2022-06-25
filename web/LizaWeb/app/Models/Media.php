<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Media extends Model
{
    use HasFactory;
    public function categories(){
        return $this->belongsToMany(Category::class, 'media_categories');
    }
}
