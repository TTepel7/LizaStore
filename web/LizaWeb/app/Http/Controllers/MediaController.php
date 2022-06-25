<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Models\Media;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Symfony\Component\HttpKernel\Exception\UnauthorizedHttpException;

class MediaController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $cat_filter= request()->input('categories', []);
        $media=Media::with('categories')->orderBy('id', 'DESC')->get();
        $media_output=[];
        foreach ($media as $m){
            $cat=[];
            foreach ($m->categories as $c){
                array_push($cat,$c->id);
            }
            if (count(array_intersect($cat_filter, $cat)) === count($cat_filter)){

                array_push($media_output,$m);

            }
        }
        return $media_output;
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function store(Request $request)
    {
        $validated= $request->validate([
           'name'=>'string|required|max:255',
           'api_token'=>'string|required',
           'description'=>'string',
           'telegram'=>'string|max:255',
            'disk_url'=>'url',
            'tags'=>'array',
            'tags.*'=>'integer|exists:categories,id'
        ]);
        if ($validated['api_token']!='qwerty52'){
            return response()->json(['error'=>'Неверный токен'],403);
        }
        $img=file_get_contents($validated['disk_url']);
        Storage::disk('public')->put($validated['name'], $img);
        $media=Media::create([
            'name'=>$validated['name'],
            'description'=>$validated['description']??'',
            'disk_url'=>'/storage/'.$validated['name'],
            'telegram'=>$validated['telegram']??''
        ]);
        foreach ($validated['tags'] as $t){
            $media->categories()->attach($t);
        }
        return $media;

    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Media  $media
     * @return \Illuminate\Http\Response
     */
    public function show(Media $media)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Media  $media
     * @return \Illuminate\Http\Response
     */
    public function edit(Media $media)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Media  $media
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Media $media)
    {
        $media['published']=!$media['published'];
        $media->save();
        return ['message'=>'ok'];
    }
    public function update_tag(Request $request, Media $media)
    {
        $validated= $request->validate([
            'name'=>'string|required|max:255']);

        $cat=Category::where('name',$validated['name'])->first();
        if(isset($cat)){
            $media->categories()->attach($cat['id']);
        }else{
            $cat=Category::create([
                'name'=>$validated['name']
            ]);
            $media->categories()->attach($cat['id']);
        }
        $media->save();
        return ['message'=>'ok'];
    }
    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Media  $media
     * @return \Illuminate\Http\Response
     */
    public function destroy(Media $media)
    {
        //
    }
}
