<template>
    <div class="container card" :class="{'loading': loading}">
        <div class="row">
            <div class="col-lg-3 mb-4 p-4">
                <div class="border border-3 p-2">
                <h1 >Фильтры</h1>

                <div class="form-check" v-for="(category, index) in categories">
                    <input class="form-check-input" type="checkbox" :value="category.id" :id="'category'+index" v-model="selected.categories">
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
                                <img class="card-img-top" :src="m.disk_url" alt="">
                            </a>
                            <div class="card-body">
                                <h4 class="card-title">
                                    <a :href="m.disk_url" target="_blank">{{ m.name }}</a>
                                </h4>
                                <p class="card-text">{{ m.description }}</p>
                                <span class="badge bg-secondary m-1" v-for="cat in m.categories">{{cat.name}}</span>
                                <p>Загружено {{new Date(m.created_at).toLocaleDateString('ru')}}</p>
                                <p v-if="m.telegram">Загружено: {{m.telegram}}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <nav class="d-flex justify-content-center">
                    <ul class="pagination pagination-lg" >
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
                page:1,
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
