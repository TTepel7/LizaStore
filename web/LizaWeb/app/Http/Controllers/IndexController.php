<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class IndexController extends Controller
{
    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        return view('index');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function upload()
    {
        return view('upload');
    }
    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function upload_store(Request $request)
    {
        $validated=$request->validate([
           'name'=>'string|required|max:255',
            'file'=>'image|required'
        ]);


        Storage::disk('yandex-disk')->put('LAbot/'.$validated['name'],  file_get_contents($validated['file']->getRealPath()));
        return redirect()->route('archive');
    }
}
