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

-- Dumping data for table chidepmp3.category: ~7 rows (approximately)
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

-- Dumping data for table chidepmp3.favorites: ~3 rows (approximately)
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
	(1, 1, 'Huu', 'Kiet', 'haha', 'hihi'),
	(2, 2, 'Dat', 'Hung', 'hoho', 'huhu'),
	(3, 3, 'Bai 3', 'Kiet', 'ahihi', 'chua co'),
	(4, 1, 'Bai 4', 'Phieu', 'chua co hinh', 'chua co mp3');

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

-- Dumping structure for table chidepmp3.user
CREATE TABLE IF NOT EXISTS `user` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table chidepmp3.user: ~2 rows (approximately)
REPLACE INTO `user` (`username`, `password`, `name`) VALUES
	('kietdang', '1', 'Kiệt Đặng'),
	('minhhuu', '1', 'Minh Hữu');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
