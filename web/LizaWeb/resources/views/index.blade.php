@extends('layouts.app')

@section('content')

    <section class="py-5 text-center container">
        <div class="row py-lg-5">
            <div class="col-lg-6 col-md-8 mx-auto card p-3">
                <h1 class="font-weight-light">Открытый архив LizaAlert</h1>
                <p class="lead text-muted">Данная страница предназначена для СМИ, здесь вы можете взять фото для публикаций с указанием авторства</p>
                <p>
                    <a href="https://lizaalert.org/" target="_blank" class="btn btn-primary my-2">Сайт LizaAlert</a>
                    <a href="{{route('archive')}}" class="btn btn-secondary my-2">Переход в закрытый архив</a>
                </p>
            </div>
        </div>
    </section>

    <div class="album py-5 bg-light">
        <div class="container">

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                    @foreach($media as $m)
                    <div class="col">
                        <div class="card shadow-sm">
                            <img class="card-img-top image_archive" src="{{$m['disk_url']}}" alt="">
                            <div class="card-body auth-form">
                                <h5 class="card-title">{{$m['name']}}</h5>
                                <a href="{{$m['disk_url']}}" target="_blank" class="btn btn-primary">Скачать</a>
                            </div>
                        </div>
                    </div>
                    @endforeach
                </div>
        </div>
    </div>
@endsection
