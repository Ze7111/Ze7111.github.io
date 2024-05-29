# ------------------------------------------------- regular imports -------------------------------------------------- #

from enum     import Enum
from pydantic import HttpUrl

# -------------------------------------------------- local imports --------------------------------------------------- #

from .pydantic_structures import TechStack                                                                 # type:ignore

# -------------------------------------------------------------------------------------------------------------------- #

class TechStackEnum(Enum): # ......................................................................................... #
    ASTRO         = TechStack(text="Astro",         alt="astro",         href=HttpUrl("https://astro.build"))
    PYTHON        = TechStack(text="Python",        alt="python",        href=HttpUrl("https://www.python.org"))
    PYDANTIC      = TechStack(text="Pydantic",      alt="pydantic",      href=HttpUrl("https://pydantic-docs.helpmanual.io"))
    FLET          = TechStack(text="Flet",          alt="flet",          href=HttpUrl("https://flet.dev"))
    GITHUB        = TechStack(text="GitHub",        alt="git_hub",       href=HttpUrl("https://github.com"))
    JAVA          = TechStack(text="Java",          alt="java",          href=HttpUrl("https://www.oracle.com/java/"))
    JAVASCRIPT    = TechStack(text="JavaScript",    alt="java_script",   href=HttpUrl("https://developer.mozilla.org/en-US/docs/Web/JavaScript"))
    TYPESCRIPT    = TechStack(text="TypeScript",    alt="type_script",   href=HttpUrl("https://www.typescriptlang.org"))
    NODEJS        = TechStack(text="Node.js",       alt="node.js",       href=HttpUrl("https://nodejs.org"))
    REACT         = TechStack(text="React",         alt="react",         href=HttpUrl("https://reactjs.org"))
    VUE           = TechStack(text="Vue",           alt="vue",           href=HttpUrl("https://vuejs.org"))
    VUEJS         = TechStack(text="Vue.js",        alt="vue.js",        href=HttpUrl("https://vuejs.org"))
    SVELTE        = TechStack(text="Svelte",        alt="svelte",        href=HttpUrl("https://svelte.dev"))
    ANGULAR       = TechStack(text="Angular",       alt="angular",       href=HttpUrl("https://angular.io"))
    RUBY          = TechStack(text="Ruby",          alt="ruby",          href=HttpUrl("https://www.ruby-lang.org"))
    RAILS         = TechStack(text="Rails",         alt="rails",         href=HttpUrl("https://rubyonrails.org"))
    PHP           = TechStack(text="PHP",           alt="php",           href=HttpUrl("https://www.php.net"))
    LARAVEL       = TechStack(text="Laravel",       alt="laravel",       href=HttpUrl("https://laravel.com"))
    DJANGO        = TechStack(text="Django",        alt="django",        href=HttpUrl("https://www.djangoproject.com"))
    FLASK         = TechStack(text="Flask",         alt="flask",         href=HttpUrl("https://flask.palletsprojects.com"))
    SPRING        = TechStack(text="Spring",        alt="spring",        href=HttpUrl("https://spring.io"))
    KOTLIN        = TechStack(text="Kotlin",        alt="kotlin",        href=HttpUrl("https://kotlinlang.org"))
    SWIFT         = TechStack(text="Swift",         alt="swift",         href=HttpUrl("https://swift.org"))
    CSHARP        = TechStack(text="C#",            alt="c#",            href=HttpUrl("https://docs.microsoft.com/en-us/dotnet/csharp/"))
    DOTNET        = TechStack(text=".NET",          alt="._net",         href=HttpUrl("https://dotnet.microsoft.com"))
    CPLUSPLUS     = TechStack(text="C++",           alt="c++",           href=HttpUrl("https://isocpp.org"))
    RUST          = TechStack(text="Rust",          alt="rust",          href=HttpUrl("https://www.rust-lang.org"))
    GO            = TechStack(text="Go",            alt="go",            href=HttpUrl("https://golang.org"))
    DOCKER        = TechStack(text="Docker",        alt="docker",        href=HttpUrl("https://www.docker.com"))
    KUBERNETES    = TechStack(text="Kubernetes",    alt="kubernetes",    href=HttpUrl("https://kubernetes.io"))
    AWS           = TechStack(text="AWS",           alt="aws",           href=HttpUrl("https://aws.amazon.com"))
    AZURE         = TechStack(text="Azure",         alt="azure",         href=HttpUrl("https://azure.microsoft.com"))
    GCP           = TechStack(text="GCP",           alt="gcp",           href=HttpUrl("https://cloud.google.com"))
    SQL           = TechStack(text="SQL",           alt="sql",           href=HttpUrl("https://en.wikipedia.org/wiki/SQL"))
    MYSQL         = TechStack(text="MySQL",         alt="my_sql",        href=HttpUrl("https://www.mysql.com"))
    POSTGRESQL    = TechStack(text="PostgreSQL",    alt="postgre_sql",   href=HttpUrl("https://www.postgresql.org"))
    MONGODB       = TechStack(text="MongoDB",       alt="mongo_db",      href=HttpUrl("https://www.mongodb.com"))
    SQLITE        = TechStack(text="SQLite",        alt="sqlite",        href=HttpUrl("https://www.sqlite.org"))
    REDIS         = TechStack(text="Redis",         alt="redis",         href=HttpUrl("https://redis.io"))
    ELASTICSEARCH = TechStack(text="Elasticsearch", alt="elasticsearch", href=HttpUrl("https://www.elastic.co"))
    TAILWINDCSS   = TechStack(text="Tailwind CSS",  alt="tailwind_css",  href=HttpUrl("https://tailwindcss.com"))
    BOOTSTRAP     = TechStack(text="Bootstrap",     alt="bootstrap",     href=HttpUrl("https://getbootstrap.com"))
    SASS          = TechStack(text="Sass",          alt="sass",          href=HttpUrl("https://sass-lang.com"))
    LESS          = TechStack(text="Less",          alt="less",          href=HttpUrl("http://lesscss.org"))
    JQUERY        = TechStack(text="jQuery",        alt="j_query",       href=HttpUrl("https://jquery.com"))
    WORDPRESS     = TechStack(text="WordPress",     alt="word_press",    href=HttpUrl("https://wordpress.org"))
    DRUPAL        = TechStack(text="Drupal",        alt="drupal",        href=HttpUrl("https://www.drupal.org"))
    JOOMLA        = TechStack(text="Joomla",        alt="joomla",        href=HttpUrl("https://www.joomla.org"))
    NEXTJS        = TechStack(text="Next.js",       alt="next.js",       href=HttpUrl("https://nextjs.org"))
    NUXTJS        = TechStack(text="Nuxt.js",       alt="nuxt.js",       href=HttpUrl("https://nuxtjs.org"))
    ZIG           = TechStack(text="Zig",           alt="zig",           href=HttpUrl("https://ziglang.org"))
    PANDAS        = TechStack(text="Pandas",        alt="pandas",        href=HttpUrl("https://pandas.pydata.org"))
    NUMPY         = TechStack(text="NumPy",         alt="num_py",        href=HttpUrl("https://numpy.org"))
    SCIKITLEARN   = TechStack(text="Scikit-learn",  alt="scikit_learn",  href=HttpUrl("https://scikit-learn.org"))
    TENSORFLOW    = TechStack(text="TensorFlow",    alt="tensor_flow",   href=HttpUrl("https://www.tensorflow.org"))
    PYTORCH       = TechStack(text="PyTorch",       alt="py_torch",      href=HttpUrl("https://pytorch.org"))
    KERAS         = TechStack(text="Keras",         alt="keras",         href=HttpUrl("https://keras.io"))
    SKLEARN       = TechStack(text="scikit-learn",  alt="scikit_learn",  href=HttpUrl("https://scikit-learn.org"))
    MATPLOTLIB    = TechStack(text="Matplotlib",    alt="matplotlib",    href=HttpUrl("https://matplotlib.org"))
    SEABORN       = TechStack(text="Seaborn",       alt="seaborn",       href=HttpUrl("https://seaborn.pydata.org"))
    BOKEH         = TechStack(text="Bokeh",         alt="bokeh",         href=HttpUrl("https://bokeh.org"))
    CUDA          = TechStack(text="CUDA",          alt="cuda",          href=HttpUrl("https://developer.nvidia.com/cuda-zone"))
    OPENCL        = TechStack(text="OpenCL",        alt="open_cl",       href=HttpUrl("https://www.khronos.org/opencl"))
    VULKAN        = TechStack(text="Vulkan",        alt="vulkan",        href=HttpUrl("https://www.khronos.org/vulkan"))
    OPENCV        = TechStack(text="OpenCV",        alt="open_cv",       href=HttpUrl("https://opencv.org"))
    PYPLOTLY      = TechStack(text="Plotly",        alt="plotly",        href=HttpUrl("https://plotly.com"))
    D3JS          = TechStack(text="D3.js",         alt="d3.js",         href=HttpUrl("https://d3js.org"))
    OPENGL        = TechStack(text="OpenGL",        alt="open_gl",       href=HttpUrl("https://www.opengl.org"))
    HTML          = TechStack(text="HTML",          alt="html",          href=HttpUrl("https://developer.mozilla.org/en-US/docs/Web/HTML"))
    CSS           = TechStack(text="CSS",           alt="css",           href=HttpUrl("https://developer.mozilla.org/en-US/docs/Web/CSS"))
    ACF           = TechStack(text="ACF",           alt="acf",           href=HttpUrl("https://www.advancedcustomfields.com"))
    R             = TechStack(text="R",             alt="r",             href=HttpUrl("https://www.r-project.org"))
# end .................................................................................................. TechStackEnum #