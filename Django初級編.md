# Django 初級編

## 初級編という事で、『CURD』

## <font color="Salmon">1. CURD</font>

- ## <font color="Salmon">Create:作成</font>
- ## <font color="Salmon">Update:更新</font>
- ## <font color="Salmon">Read:読み込み</font>
- ## <font color="Salmon">Delete:削除</font>

## <font color="Crimson">2. ユーザ認証</font>

- ## <font color="Crimson">Login</font>
- ## <font color="Crimson">Logout</font>

## 上記の機能を持った Web アプリケーションを作っていきたいと思います。

### 基本的な Django の機能を使用していきますので、Web アプリケーション作成する

### イメージを持って頂ければ幸いです。

---

## 3. Project 作成

- ## <font color="DarkGoldenRod">django-admin startproject</font>

  ### 以下のコマンド Django Project を作成します。

  ### <font color="OrangeRed">django-admin startproject config .</font>

## 4. アプリケーション作成

- ## <font color="DarkGoldenRod">startapp [AppName]</font>

  ### 以下のコマンドでアプリケーションを作成します。

  ### <font color="OrangeRed">./manage.py startapp [AppName]</font>

  ### 最初は、急にファイルが沢山できて混乱してしまうかもしれませんが

  ### 本来は、個別に作成すべきファイルを、Django が変わりに作ってくれています。

  ### これが**フレームワーク**の良い所です。

---

- ## 「setting.py」の 変更

  - ### <font color="DarkKhaki">INSTALLED_APPS</font> : アプリケーションを追加する
  - ### <font color="DarkKhaki">LANGUAGE_CODE</font> : Admin 画面の言語を変更する
  - ### <font color="DarkKhaki">TIME_ZONE</font> : タイムゾーンを変更する

---

## 5. モデル作成

### ORM（Object Relational Mapper）

### ザックリいうと Python などの**オブジェクト指向**の言語を**データベース**の言語に変換してくれる。

### **Database** を変更しても、**コードを変更**しなくても良い。

### 例えば、開発時は自分の PC の**SQLite**で行う事が多いですが、

### 本番環境などでは、本格的な**Database**を導入する事がほとんどだと思います。

https://docs.djangoproject.com/ja/3.0/misc/design-philosophies/#dry

---

### **mdels.py の内容を変更**した場合、**マイグレーション**をする必要があります。

### マイグレーションをするには以下のコマンドを実行します。

- ### <font color="OrangeRed">./manage.py makemigrations</font>

### 次に、マイグレートを実施する事で、データベースに反映させます。

- ### <font color="OrangeRed">./manage.py migrate</font>

### <font color="DarkOrange">Makemigrations</font> / <font color="DarkOrange">Migrate</font> とは？

- ### <font color="DarkOrange">Makemigrations</font>
  - ### マイグレーションファイルを作成する
    - ### データベース構成のバージョン管理をするのにマイグレーションファイルを作成する。
- ### <font color="DarkOrange">Migrate</font>
  - ### モデルをデータベースに反映させる
    - ### データベース構成を変更したり、その変更を取り消したりすることが出来る。

### データベースを作ったので、データを入れていきます。

### 後でサイトからデータを保存できるようにします。

### まだ、その機能を作っていないので、Admin 画面を使いたいと思います。

---

## 6. Admin 画面

### Admin 画面を使うには、管理者の登録が必要になります。

### 以下のコマンドで、管理者を登録します。

- ### <font color="OrangeRed">./manage.py createsuperuser</font>

### Admin 画面に行くには、開発サーバを立ち上げる必要がありますので、以下のコマンドを実行してください。

- ### <font color="OrangeRed">./manage.py runserver</font>

### Admin 画面で、作成したモデルを表示するには、admin.py を変更する必要があります。

### admin.py を変更後、Admin 画面をリフレッシュするとモデルが表示されます。

### title = models.CharField(verbose_name="アルバム名", max_length=512)

## 7. View

### urls.py に追加。

### Class-Based Views の場合、as_view()を付加する

### 例) path('', PostListView.**as_view()**),

### Class-Based Views の場合は機能追加のために、Mix-in が多用されます。

- ### Mix-in とはインスタンス変数を持たずメソッドだけを定義したクラス
- ### 継承されることを前提
- ### Mix-in を好きなだけ継承することでサブクラスで必要な機能を追加する、といった使い方をします

## 8. Frontend

### 全て１から作っていくには、初級編としては作業量が多すぎてしまうので
### Homeのページはテンプレートを使っていきます。
### テンプレートを入れる前の下準備からしていきます。
### CSS, Javascript, img画像が含まれているので、それぞれのフォルダを作成していきます。
### settings.pyを開いて一番下までいってください。

- ### STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

### staticはWebサイト内で統一した方が、見栄えが良いです。

### 今作っているブログは自分専用になっていますので、他の人も書き込めるようにします。
### そのためにはユーザ登録が必要になります。ユーザ登録には何が必要か考えてみましょう。
### ユーザ登録するフォームがいりますよね。
### ユーザ登録関連をブログの中に作る事は可能ですが、別にアプリを作った方が管理しやすいので
### 別のアプリを作っていきましょう。
### 新しいアプリを作った場合、settings.pyに追加する必要があります。

## 9. サインアップ

### 一からユーザ登録のフォームを作るとしたら、パスワードなど確認することが沢山あります。
### それを簡単してくれる物がDjangoにはあります。

- ### from django.contrib.auth.forms import UserCreationForm

### 7 Crispy Forms

### 一番簡単なのは
### {{ form }} --> {{ form.as_p }}
### form パラグラフと同じタグ <p> 段落になります

### まだ、ゴチャゴチャしていて、カッコよくないですね
### その場合は、新しくCrispy Formsというものを入れます。
- ### pip install django-crispy-forms
### settings.pyに追加する（INSTALLED_APPS）
- ### 'crispy_forms', # 追加する
### settings.pyに追加する（一番したの方に）
### bootstrapは現在最新は、bootstrap4.xになりますが
### ダウンロードしたテンプレートがbootstrap3を使用しているため
### 今回はbootstrap3をしてします
- ### CRISPY_TEMPLATE_PACK = 'bootstrap3' # 追加する

### {% load crispy_forms_tags %} # 追加する
### {{ form.as_p }} --> {{ form|crispy }}

### ドキュメント
- ### https://docs.djangoproject.com/ja/3.0/contents/

## 10. Login Logout

### account -> urls.py に追加する
### フレームワークでLogin-Logoutが提供されている

- ### from django.contrib.auth import views as auth_views # 追加
- ### path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
- ### path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),

### キャメルケース、スネークケース  あくまでもルールとして

### login logout を作っていきましょう

### loginすると、以下のエラーが発生する
### Request URL:	http://127.0.0.1:8000/accounts/profile/    
### Djangoのデフォルト設定でログインした後に、profileのページに遷移するようになっている
### settings.py に 以下を追加する

- ### LOGIN_REDIRECT_URL = 'blog-home'
- ### views.py redirectをloginに変更する（登録したらLoginページへ遷移させる）
- ### base.html login リンクを修正する
