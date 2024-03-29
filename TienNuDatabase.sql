-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.22-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for chidepmp3
CREATE DATABASE IF NOT EXISTS `chidepmp3` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `chidepmp3`;

-- Dumping structure for table chidepmp3.category
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.category: ~6 rows (approximately)
REPLACE INTO `category` (`id`, `title`) VALUES
	(1, 'Nhạc trữ tình'),
	(2, 'EDM'),
	(3, 'Remix'),
	(4, 'Hip hop'),
	(5, 'Acoustic'),
	(6, 'US-UK'),
	(7, 'Nhạc trẻ');

-- Dumping structure for table chidepmp3.favorites
CREATE TABLE IF NOT EXISTS `favorites` (
  `userID` varchar(50) DEFAULT NULL,
  `songID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.favorites: ~2 rows (approximately)
REPLACE INTO `favorites` (`userID`, `songID`) VALUES
	('kietdang', 2),
	('minhhuu', 3),
	('kietdang', 1);

-- Dumping structure for table chidepmp3.music
CREATE TABLE IF NOT EXISTS `music` (
  `id` int(11) DEFAULT NULL,
  `category` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `artist` varchar(50) DEFAULT NULL,
  `img` varchar(50) DEFAULT NULL,
  `file` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.music: ~4 rows (approximately)
REPLACE INTO `music` (`id`, `category`, `name`, `artist`, `img`, `file`) VALUES
	(1, 1, 'Huu', 'Kiet', 'album1.jfif', 'tabun.mp3'),
	(2, 2, 'Dat', 'Hung', 'song2.jfif', 'tabun.mp3'),
	(3, 3, 'Bai 3', 'Kiet', 'song3.jfif', 'test.mp3'),
	(4, 1, 'Bai 4', 'Phieu', 'song4.jfif', 'test.mp3');

-- Dumping structure for table chidepmp3.playlist
CREATE TABLE IF NOT EXISTS `playlist` (
  `id` int(11) DEFAULT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `playlistTitle` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.playlist: ~2 rows (approximately)
REPLACE INTO `playlist` (`id`, `userid`, `playlistTitle`) VALUES
	(1, 'kietdang', 'chill'),
	(2, 'kietdang', 'anime');

-- Dumping structure for table chidepmp3.playlistdetail
CREATE TABLE IF NOT EXISTS `playlistdetail` (
  `playlistID` int(11) DEFAULT NULL,
  `songID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.playlistdetail: ~6 rows (approximately)
REPLACE INTO `playlistdetail` (`playlistID`, `songID`) VALUES
	(1, 1),
	(1, 2),
	(1, 3),
	(2, 2),
	(2, 3),
	(2, 4);

-- Dumping structure for table chidepmp3.slide
CREATE TABLE IF NOT EXISTS `slide` (
  `slideID` int(11) NOT NULL AUTO_INCREMENT,
  `slideTitle` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`slideID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.slide: ~4 rows (approximately)
REPLACE INTO `slide` (`slideID`, `slideTitle`) VALUES
	(1, 'Nhạc hot mùa hè'),
	(2, 'Nhạc trẻ'),
	(3, 'Hot gần đây'),
	(4, 'Chill');

-- Dumping structure for table chidepmp3.slidedetail
CREATE TABLE IF NOT EXISTS `slidedetail` (
  `slideID` int(11) DEFAULT NULL,
  `songid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.slidedetail: ~8 rows (approximately)
REPLACE INTO `slidedetail` (`slideID`, `songid`) VALUES
	(1, 1),
	(1, 2),
	(2, 2),
	(2, 3),
	(3, 1),
	(3, 3),
	(4, 4),
	(4, 1);

-- Dumping structure for table chidepmp3.user
CREATE TABLE IF NOT EXISTS `user` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `createdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.user: ~2 rows (approximately)
REPLACE INTO `user` (`username`, `password`, `name`, `createdate`) VALUES
	('kietdang', '1', 'Kiệt Đặng', '2024-03-22'),
	('minhhuu', '1', 'Minh Hữu', '2024-03-22');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
