node{
    stage("Checkout"){
     git"https://github.com/Michaell99/World-Of-Games.git"
    }
    stage("Build"){
        bat "docker compose up -d"
    }
    stage("Test"){
        bat "python Test/e2e.py"
    }
    stage("Push"){
        bat "docker tag worldofgame_test_web michaelliav/worldofgames:v1"
        bat "docker push michaelliav/worldofgames:v1"
    }
}