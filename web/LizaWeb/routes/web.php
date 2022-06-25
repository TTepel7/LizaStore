<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/



Auth::routes(['register' => false]);

Route::get('/', [App\Http\Controllers\IndexController::class, 'index'])->name('index');
Route::get('/upload', [App\Http\Controllers\IndexController::class, 'upload'])->name('upload');
Route::post('/upload', [App\Http\Controllers\IndexController::class, 'upload_store'])->name('upload_store');
Route::get('/archive', [App\Http\Controllers\HomeController::class, 'index'])->name('archive');
