from flask import Flask, render_template
from classes.course import Course

app = Flask(__name__)

@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html", description = "A página que você tentou acessar não pode ser encontrada.") 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/news')
def news():
    title = "Funcionários usam IA generativa para lidar com excesso de trabalho"
    paragraph = "Segundo 75% dos trabalhadores intelectuais ouvidos, IA no trabalho já é uma realidade – no Brasil o índice sobe para 83%. A principal razão para isso é, segundo os próprios colaboradores, o ritmo e o volume de trabalho excessivo, e a IA os ajuda a economizar tempo para se dedicar em atividades mais relevantes."
    return render_template("news.html", title = title, paragraph = paragraph)

@app.route('/courses')
def courses():
    courses = ['Computação em Nuvem', 'Data Science', 'Engenharia de Software', 'Inteligência Artificial']
    return render_template("courses.html", courses = courses)

@app.route('/courses/<name>')
def course(name):
    if name == 'computacao-em-nuvem':
        course = Course('Computação em Núvem', ['Cloud Solutions Architect', 'Devops', 'Machine Learning'],'Desenvolver as principais soluções de Computação em Nuvem Pública e Privada do mercado. Dominar os conceitos e técnicas de infraestrutura como código. Planejar e implementar um ambiente mais eficiente com formatos de elasticidades e custos definidos. Conhecer e aplicar uma nova cultura DEVOPS, além de conceitos de automação e orquestração de microsserviços através de Containers & Kubernetes. Avaliar os aspectos estratégicos dos provedores de nuvem, além da visão técnica. Implementar a Computação em Nuvem, com suas diversas camadas de serviços. Integrar soluções para composição de nuvens híbridas, alinhando e melhorando a segurança dos processos com automação via Cloud Security.')
        return render_template("course.html", course = course)
    elif name == 'data-science':
        course = Course('Data Science', ['Big Data', 'BI', 'Data Engineering'], 'Aprender conceitos como modelagem de dados (relacionais, dimensionais e estatísticos), linguagens de programação (SQL e Python), ferramentas de visualização de dados, ferramentas de análise e qualificação de dados. Também vai se aprofundar em: Cloud, NoSQL, Data Warehouse, Data Lake, Lake Warehouse, Big Data, Machine Learning, Deep Learning, Data Mining, Data Analytics, Data Viz, IA Generativas, Data Driven, Data Governance e LGPD. Desenvolver habilidades de comunicação para apresentar suas descobertas e insights de forma clara e acessível para públicos não técnicos.')
        return render_template("course.html", course = course)
    elif name == 'engenharia-de-software':
        course = Course('Engenharia de Software', ['High Performance System', 'Advanced Computing', 'Smart Society'], 'Você dominará os conhecimentos mais avançados em linguagens de programação para atuar como desenvolvedor Full Stack, podendo exercer a função de um DevSecOps e contando com a possibilidade de aplicar conceitos de Data Driven Specialist em seu trabalho, tornando-se o perfil de engenheiro melhor preparado para o atual cenário dentro das organizações.')
        return render_template("course.html", course = course)
    elif name == 'inteligencia-artificial':
        course = Course('Inteligência Artificial', ['Machine Learnig', 'IA Generativa', 'Natural Language Processing'], 'Explorar e aplicar técnicas de Machine Learning e Deep Learning como diferencial competitivo das empresas. Desenvolver chatbots que interpretem a linguagem natural, imagens e sons, otimizando o atendimento ao cliente. E dominar as tecnologias disruptivas que estão mudando o mundo, como robôs autônomos, sistemas preditivos, dispositivos wearable e muito mais. Com tantas novas skills, você se prepara para liderar a transformação digital das empresas. Afinal, a Inteligência Artificial e suas aplicações aceleram inevitavelmente esse processo.')
        return render_template("course.html", course = course)




""" @app.route('/courses/<name>')
def course(name):
    if name == 'computacao-em-nuvem':
        course = Course('Computação em Núvem', ['Cloud Solutions Architect', 'Devops', 'Machine Learning'],'Desenvolver as principais soluções de Computação em Nuvem Pública e Privada do mercado. Dominar os conceitos e técnicas de infraestrutura como código. Planejar e implementar um ambiente mais eficiente com formatos de elasticidades e custos definidos. Conhecer e aplicar uma nova cultura DEVOPS, além de conceitos de automação e orquestração de microsserviços através de Containers & Kubernetes. Avaliar os aspectos estratégicos dos provedores de nuvem, além da visão técnica. Implementar a Computação em Nuvem, com suas diversas camadas de serviços. Integrar soluções para composição de nuvens híbridas, alinhando e melhorando a segurança dos processos com automação via Cloud Security.')
        # skills = ['Cloud Solutions Architect', 'Devops', 'Machine Learning']
        return render_template("course.html", course = course)
        # return render_template("course.html", course = course, skills = skills)
    elif name == 'data-science':
        course = Course('Data Science', 'Aprender conceitos como modelagem de dados (relacionais, dimensionais e estatísticos), linguagens de programação (SQL e Python), ferramentas de visualização de dados, ferramentas de análise e qualificação de dados. Também vai se aprofundar em: Cloud, NoSQL, Data Warehouse, Data Lake, Lake Warehouse, Big Data, Machine Learning, Deep Learning, Data Mining, Data Analytics, Data Viz, IA Generativas, Data Driven, Data Governance e LGPD. Desenvolver habilidades de comunicação para apresentar suas descobertas e insights de forma clara e acessível para públicos não técnicos.')
        skills = ['Big Data', 'BI', 'Data Engineering']
        return render_template("course.html", course = course, skills = skills)
    elif name == 'engenharia-de-software':
        course = Course('Engenharia de Software', 'Você dominará os conhecimentos mais avançados em linguagens de programação para atuar como desenvolvedor Full Stack, podendo exercer a função de um DevSecOps e contando com a possibilidade de aplicar conceitos de Data Driven Specialist em seu trabalho, tornando-se o perfil de engenheiro melhor preparado para o atual cenário dentro das organizações.')
        skills = ['High Performance System', 'Advanced Computing', 'Smart Society']
        return render_template("course.html", course = course, skills = skills)
    elif name == 'inteligencia-artificial':
        course = Course('Inteligência Artificial', 'Explorar e aplicar técnicas de Machine Learning e Deep Learning como diferencial competitivo das empresas. Desenvolver chatbots que interpretem a linguagem natural, imagens e sons, otimizando o atendimento ao cliente. E dominar as tecnologias disruptivas que estão mudando o mundo, como robôs autônomos, sistemas preditivos, dispositivos wearable e muito mais. Com tantas novas skills, você se prepara para liderar a transformação digital das empresas. Afinal, a Inteligência Artificial e suas aplicações aceleram inevitavelmente esse processo.')
        skills = ['Machine Learnig', 'IA Generativa', 'Natural Language Processing']
        return render_template("course.html", course = course, skills = skills)
    else:
        return render_template("404.html", description = "A página que você tentou acessar não pode ser encontrada.") """




""" @app.route('/courses/<name>')
def course(name):
    if name == 'computacao-em-nuvem':
        skills = ['Cloud Solutions Architect', 'Devops', 'Machine Learning']
        return render_template("course.html", course = course, skills = skills, description = "Desenvolver as principais soluções de Computação em Nuvem Pública e Privada do mercado. Dominar os conceitos e técnicas de infraestrutura como código. Planejar e implementar um ambiente mais eficiente com formatos de elasticidades e custos definidos. Conhecer e aplicar uma nova cultura DEVOPS, além de conceitos de automação e orquestração de microsserviços através de Containers & Kubernetes. Avaliar os aspectos estratégicos dos provedores de nuvem, além da visão técnica. Implementar a Computação em Nuvem, com suas diversas camadas de serviços. Integrar soluções para composição de nuvens híbridas, alinhando e melhorando a segurança dos processos com automação via Cloud Security.")
    elif name == 'data-science':
        skills = ['Big Data', 'BI', 'Data Engineering']
        return render_template("course.html", course = "Data Science", skills = skills, description = "Aprender conceitos como modelagem de dados (relacionais, dimensionais e estatísticos), linguagens de programação (SQL e Python), ferramentas de visualização de dados, ferramentas de análise e qualificação de dados. Também vai se aprofundar em: Cloud, NoSQL, Data Warehouse, Data Lake, Lake Warehouse, Big Data, Machine Learning, Deep Learning, Data Mining, Data Analytics, Data Viz, IA Generativas, Data Driven, Data Governance e LGPD. Desenvolver habilidades de comunicação para apresentar suas descobertas e insights de forma clara e acessível para públicos não técnicos.")
    elif name == 'engenharia-de-software':
        skills = ['High Performance System', 'Advanced Computing', 'Smart Society']
        return render_template("course.html", course = "Engenharia de Software", skills = skills, description = "Você dominará os conhecimentos mais avançados em linguagens de programação para atuar como desenvolvedor Full Stack, podendo exercer a função de um DevSecOps e contando com a possibilidade de aplicar conceitos de Data Driven Specialist em seu trabalho, tornando-se o perfil de engenheiro melhor preparado para o atual cenário dentro das organizações.")
    elif name == 'inteligencia-artificial':
        skills = ['Machine Learnig', 'IA Generativa', 'Natural Language Processing']
        return render_template("course.html", course = "Inteligência Artificial", skills = skills, description = "Explorar e aplicar técnicas de Machine Learning e Deep Learning como diferencial competitivo das empresas. Desenvolver chatbots que interpretem a linguagem natural, imagens e sons, otimizando o atendimento ao cliente. E dominar as tecnologias disruptivas que estão mudando o mundo, como robôs autônomos, sistemas preditivos, dispositivos wearable e muito mais. Com tantas novas skills, você se prepara para liderar a transformação digital das empresas. Afinal, a Inteligência Artificial e suas aplicações aceleram inevitavelmente esse processo.")
    else:
        return render_template("404.html", description = "A página que você tentou acessar não pode ser encontrada.") """