cmake_minimum_required(VERSION 3.15)
project(dt_resources)

set(COMMON_DIRECTORIES
  configs
  mesh
  ontologies
  textures
)

if($ENV{ROS_VERSION} STREQUAL "1")
  find_package(catkin REQUIRED)

  catkin_package()

  install(DIRECTORY launch/ DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch)

  foreach(dir ${COMMON_DIRECTORIES})
    install(DIRECTORY ${dir}/ DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
  endforeach()

elseif($ENV{ROS_VERSION} STREQUAL "2")

  find_package(ament_cmake REQUIRED)

  install(DIRECTORY launch2/ DESTINATION share/${PROJECT_NAME}/launch)

  foreach(dir ${COMMON_DIRECTORIES})
    install(DIRECTORY ${dir}/ DESTINATION share/${PROJECT_NAME}/${dir})
  endforeach()

  ament_package()

else()
  message(FATAL_ERROR "Unsupported ROS version: $ENV{ROS_VERSION}")
endif()
