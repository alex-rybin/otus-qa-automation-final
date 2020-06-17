pipeline {
    agent any

    environment {
        PROJECT_NAME = 'otus-qa-automation-final'
    }

    stages {
        stage('Get data') {
            steps {
                echo "Getting branch ${ghprbSourceBranch} from repository"
                dir("${WORK_FOLDER}") {
                    sh "git clone https://github.com/alex-rybin/${PROJECT_NAME}.git"
                }
                dir("${WORK_FOLDER}/${PROJECT_NAME}") {
                    sh "git checkout ${ghprbSourceBranch}"
                }
            }
        }
        stage('Prepare environment') {
            steps {
                echo 'Preparing environment'
                dir("${WORK_FOLDER}/${PROJECT_NAME}") {
                    sh 'docker-compose up -d'
                }
            }
        }
        stage ('Build tests') {
            steps {
                echo 'Building tests'
                dir("${WORK_FOLDER}/${PROJECT_NAME}") {
                    sh 'docker build -t prestashop-tests .'
                }
            }
        }
        stage ('Run tests') {
            steps {
                dir("${WORK_FOLDER}/${PROJECT_NAME}") {
                    script {
                        try {
                            echo 'Running tests'
                            sh "docker run -v ${WORK_FOLDER}/${PROJECT_NAME}/allure-results:/app/allure-results --name ${PROJECT_NAME}_tests_1 --network ${PROJECT_NAME}_default prestashop-tests"
                        } finally {
                            echo 'Collecting report'
                            allure([
                                includeProperties: false,
                                jdk: '',
                                properties: [],
                                reportBuildPolicy: 'ALWAYS',
                                results: [[path: 'allure-results']]
                            ])
                            stage('Teardown') {
                                steps {
                                    echo 'Clearing up'
                                    dir("${WORK_FOLDER}/${PROJECT_NAME}") {
                                        sh 'docker-compose down'
                                    }
                                    dir("${WORK_FOLDER}") {
                                        sh "rm -rfv *"
                                    }
                                    sh "docker rm ${PROJECT_NAME}_tests_1"
                                    sh 'docker rmi prestashop-tests'
                                    sh "docker volume rm ${PROJECT_NAME}_mariadb_data"
                                    sh "docker volume rm ${PROJECT_NAME}_prestashop_data"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
