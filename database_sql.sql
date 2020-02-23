-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.4.12-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- swstats 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `swstats` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `swstats`;

-- 테이블 swstats.auth_group 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.auth_group:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- 테이블 swstats.auth_group_permissions 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.auth_group_permissions:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- 테이블 swstats.auth_permission 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.auth_permission:~32 rows (대략적) 내보내기
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add question', 7, 'add_question'),
	(26, 'Can change question', 7, 'change_question'),
	(27, 'Can delete question', 7, 'delete_question'),
	(28, 'Can view question', 7, 'view_question'),
	(29, 'Can add choice', 8, 'add_choice'),
	(30, 'Can change choice', 8, 'change_choice'),
	(31, 'Can delete choice', 8, 'delete_choice'),
	(32, 'Can view choice', 8, 'view_choice');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- 테이블 swstats.auth_user 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.auth_user:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$180000$BVRT21dQwQGi$+cmz2jmmUMMbs1O5JfD+7ssNLFj7a2mHGZ8f6Z4uI2c=', '2020-02-22 10:38:07.576223', 1, 'admin', '', '', 'mayu1989@naver.com', 1, 1, '2020-02-16 07:00:05.635577');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- 테이블 swstats.auth_user_groups 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.auth_user_groups:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- 테이블 swstats.auth_user_user_permissions 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.auth_user_user_permissions:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- 테이블 swstats.django_admin_log 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.django_admin_log:~3 rows (대략적) 내보내기
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2020-02-16 08:03:56.218004', '1', 'What is your developer role?', 1, '[{"added": {}}, {"added": {"name": "choice", "object": "Developer, full-stack"}}, {"added": {"name": "choice", "object": "Developer, back-end"}}, {"added": {"name": "choice", "object": "Developer, front-end"}}, {"added": {"name": "choice", "object": "Developer, mobile"}}, {"added": {"name": "choice", "object": "Database administrator"}}, {"added": {"name": "choice", "object": "Developer, embedded applications or devices"}}, {"added": {"name": "choice", "object": "Data scientist or machine learning specialist"}}, {"added": {"name": "choice", "object": "Database administrator"}}, {"added": {"name": "choice", "object": "student"}}, {"added": {"name": "choice", "object": "etc"}}]', 7, 1),
	(2, '2020-02-16 08:06:15.943808', '2', 'work experience', 1, '[{"added": {}}, {"added": {"name": "choice", "object": "less than 5 years"}}, {"added": {"name": "choice", "object": "5 to 9 years"}}, {"added": {"name": "choice", "object": "10 to 14 years"}}, {"added": {"name": "choice", "object": "15 to 19 years"}}, {"added": {"name": "choice", "object": "20 to 24 years"}}, {"added": {"name": "choice", "object": "more than 25 years"}}]', 7, 1),
	(3, '2020-02-22 11:50:39.155339', '3', 'How much do you make per year?', 1, '[{"added": {}}, {"added": {"name": "choice", "object": "less than US$ 40,000 /yr"}}, {"added": {"name": "choice", "object": "US$ 40,000 ~60,000 /yr"}}, {"added": {"name": "choice", "object": "US$ 60,000 ~80,000 /yr"}}, {"added": {"name": "choice", "object": "US$ 80,000 ~100,000 /yr"}}, {"added": {"name": "choice", "object": "US$ 100,000 ~120,000 /yr"}}, {"added": {"name": "choice", "object": "US$ 120,000 ~140,000 /yr"}}, {"added": {"name": "choice", "object": "over US$ 140,000 /yr"}}]', 7, 1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- 테이블 swstats.django_content_type 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.django_content_type:~8 rows (대략적) 내보내기
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(8, 'polls', 'choice'),
	(7, 'polls', 'question'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- 테이블 swstats.django_migrations 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.django_migrations:~22 rows (대략적) 내보내기
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2020-02-16 06:53:20.202280'),
	(2, 'auth', '0001_initial', '2020-02-16 06:53:20.784665'),
	(3, 'admin', '0001_initial', '2020-02-16 06:53:22.389306'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2020-02-16 06:53:22.784212'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-02-16 06:53:22.822113'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2020-02-16 06:53:23.091442'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2020-02-16 06:53:23.275925'),
	(8, 'auth', '0003_alter_user_email_max_length', '2020-02-16 06:53:23.578181'),
	(9, 'auth', '0004_alter_user_username_opts', '2020-02-16 06:53:23.663914'),
	(10, 'auth', '0005_alter_user_last_login_null', '2020-02-16 06:53:23.837392'),
	(11, 'auth', '0006_require_contenttypes_0002', '2020-02-16 06:53:23.846406'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2020-02-16 06:53:23.879279'),
	(13, 'auth', '0008_alter_user_username_max_length', '2020-02-16 06:53:23.939169'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2020-02-16 06:53:23.995017'),
	(15, 'auth', '0010_alter_group_name_max_length', '2020-02-16 06:53:24.188647'),
	(16, 'auth', '0011_update_proxy_permissions', '2020-02-16 06:53:24.223368'),
	(17, 'polls', '0001_initial', '2020-02-16 06:53:24.400923'),
	(18, 'polls', '0002_auto_20200128_1439', '2020-02-16 06:53:24.485662'),
	(19, 'polls', '0003_choice_question', '2020-02-16 06:53:24.601414'),
	(20, 'polls', '0004_auto_20200128_1606', '2020-02-16 06:53:24.685172'),
	(21, 'polls', '0005_choice_question', '2020-02-16 06:53:24.842770'),
	(22, 'sessions', '0001_initial', '2020-02-16 06:53:25.152880');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- 테이블 swstats.django_session 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.django_session:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('ac9jhpazvkllmr5nn71axc6fo85ow5u0', 'MDk4ODM3MDI4OTg1ZWFjMjhiNDMwNWQ3MTlmM2JjOTlmZTJlNmFjMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYTQzYjk2NGNkYjlmNmUzZGM4MTEzMmE2NjJiZWQxMzcwNTE1ZTgxIn0=', '2020-03-07 10:38:07.589220'),
	('as7gm0bdnvwshtg2zmsu0yf5o3nfgycp', 'MDk4ODM3MDI4OTg1ZWFjMjhiNDMwNWQ3MTlmM2JjOTlmZTJlNmFjMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYTQzYjk2NGNkYjlmNmUzZGM4MTEzMmE2NjJiZWQxMzcwNTE1ZTgxIn0=', '2020-03-01 07:01:30.408695');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- 테이블 swstats.polls_choice 구조 내보내기
CREATE TABLE IF NOT EXISTS `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` varchar(100) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`),
  CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.polls_choice:~17 rows (대략적) 내보내기
/*!40000 ALTER TABLE `polls_choice` DISABLE KEYS */;
INSERT INTO `polls_choice` (`id`, `choice_text`, `votes`, `question_id`) VALUES
	(1, 'Developer, full-stack', 1, 1),
	(2, 'Developer, back-end', 0, 1),
	(3, 'Developer, front-end', 0, 1),
	(4, 'Developer, mobile', 0, 1),
	(5, 'Database administrator', 0, 1),
	(6, 'Developer, embedded applications or devices', 0, 1),
	(7, 'Data scientist or machine learning specialist', 0, 1),
	(8, 'Database administrator', 0, 1),
	(9, 'student', 0, 1),
	(10, 'etc', 0, 1),
	(17, 'less than US$ 40,000 /yr', 0, 3),
	(18, 'US$ 40,000 ~60,000 /yr', 0, 3),
	(19, 'US$ 60,000 ~80,000 /yr', 0, 3),
	(20, 'US$ 80,000 ~100,000 /yr', 0, 3),
	(21, 'US$ 100,000 ~120,000 /yr', 0, 3),
	(22, 'US$ 120,000 ~140,000 /yr', 0, 3),
	(23, 'over US$ 140,000 /yr', 0, 3);
/*!40000 ALTER TABLE `polls_choice` ENABLE KEYS */;

-- 테이블 swstats.polls_question 구조 내보내기
CREATE TABLE IF NOT EXISTS `polls_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 테이블 데이터 swstats.polls_question:~3 rows (대략적) 내보내기
/*!40000 ALTER TABLE `polls_question` DISABLE KEYS */;
INSERT INTO `polls_question` (`id`, `question_text`, `pub_date`) VALUES
	(1, 'What is your developer role?', '2020-02-16 07:06:00.000000'),
	(3, 'How much do you make per year?', '2020-02-22 11:46:04.000000');
/*!40000 ALTER TABLE `polls_question` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
