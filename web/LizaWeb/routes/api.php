<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('categories', [\App\Http\Controllers\CategoryController::class,'index']);
Route::get('media', [\App\Http\Controllers\MediaController::class,'index']);
Route::post('media', [\App\Http\Controllers\MediaController::class,'store']);
Route::put('media/pub/{media}', [\App\Http\Controllers\MediaController::class,'update']);
Route::put('media/tag/{media}', [\App\Http\Controllers\MediaController::class,'update_tag']);
