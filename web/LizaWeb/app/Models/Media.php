<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Media extends Model
{
    use HasFactory;
    protected $fillable = ['name', 'description', 'telegram', 'disk_url','published'];
    public function categories(){
        return $this->belongsToMany(Category::class, 'media_categories');
    }
}
