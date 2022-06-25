<template>
    <div class="container card" :class="{'loading': loading}">
        <div class="row">
            <div class="col-lg-3 mb-4 p-4">
                <div class="border border-3 p-2">
                    <h1>Фильтры</h1>
                    <div class="mb-2">
                        <h5>Год</h5>
                        <select class="form-select form-select-sm" aria-label=".form-select-sm example">
                            <option selected>Выбрать год</option>
                            <option value="2020">2020</option>
                            <option value="2021">2021</option>
                            <option value="2022">2022</option>
                            <option value="2023">2023</option>
                        </select>
                    </div>
                    <div class="form-check" v-for="(category, index) in categories">
                        <input class="form-check-input" type="checkbox" :value="category.id" :id="'category'+index"
                               v-model="selected.categories">
                        <label class="form-check-label" :for="'category' + index">
                            {{ category.name }} ({{ category.media_count }})
                        </label>
                    </div>
                </div>

            </div>
            <div class="col-lg-9">
                <h1 class="mt-4">Результаты поиска <span style="color: gray;">({{media.length}})</span></h1>
                <div class="row mt-4">
                    <div class="col-lg-4 col-md-6 mb-4" v-for="(m,index) in media.slice((page-1)*9,(page-1)*9+9)">
                        <div class="card h-100">
                            <a href="#">
                                <img class="card-img-top image_archive" :src="m.disk_url" alt="">
                            </a>
                            <div class="card-body">
                                <h4 class="card-title">
                                    <a :href="m.disk_url" target="_blank">{{ m.name }}</a>
                                </h4>
                                <a v-if="m.description" :href="m.description" target="_blank">Гео метка</a>
                                <span class="badge bg-secondary m-1" v-for="cat in m.categories">{{cat.name}}</span>
                                <span class="badge bg-secondary m-1" @click="add_tag(m.id)">+</span>
                                <p class="mb-0" v-if="m.telegram" >Загружено: {{m.telegram}}</p>
                                <p class="mb-0">Загружено {{new Date(m.created_at).toLocaleDateString('ru')}}</p>
                                <div class="form-check" >
                                    <input class="form-check-input" type="checkbox" :id="'public'+m.id" v-model="m.published" @change="set_published(m.id)">
                                    <label class="form-check-label" :for="'public' + m.id">
                                        Публикация для СМИ
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <nav class="d-flex justify-content-center">
                    <ul class="pagination pagination-lg">
                        <li class="page-item" :class="{'disabled':page===p}" v-for="p in Math.ceil(media.length/9)">
                            <a class="page-link" href="#" @click="page=p">{{p}}</a>
                        </li>
                    </ul>
                </nav>

            </div>


        </div>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                categories: [],
                media: [],
                loading: true,
                page: 1,
                selected: {
                    prices: [],
                    categories: [],
                    manufacturers: []
                }
            }
        },

        mounted() {
            this.loadCategories();
            this.loadMedia();
        },

        watch: {
            selected: {
                handler: function () {
                    this.loadMedia();
                },
                deep: true
            }
        },

        methods: {
            add_tag(id){
              let tag_name=prompt('Введите название тэга');
                axios.put('/api/media/tag/'+id,{
                    'name':tag_name
                })
                    .then((response) => {
                        this.loadCategories();
                        this.loadMedia();
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },
            set_published(id){

                axios.put('/api/media/pub/'+id)
                    .then((response) => {
                        //
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },
            loadCategories: function () {
                axios.get('/api/categories')
                    .then((response) => {
                        this.categories = response.data;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },

            loadMedia: function () {
                axios.get('/api/media', {
                    params: this.selected
                })
                    .then((response) => {
                        this.media = response.data;
                        this.loading = false;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },


        }
    }
</script>
