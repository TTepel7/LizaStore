<?php

namespace App\Http\Controllers;

use App\Models\Media;
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
        $media=Media::where('published',1)->take(9)->get();
        return view('index')->with('media',$media);
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
            'file'=>'image|required'
        ]);

        Storage::disk('yandex-disk')->put('LAbot/'.$validated['file']->getClientOriginalName(),  file_get_contents($validated['file']->getRealPath()));
        return redirect()->route('archive');
    }
}
