-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 20-Maio-2022 às 12:18
-- Versão do servidor: 10.1.38-MariaDB
-- versão do PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud_filmes`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes`
--

CREATE TABLE `filmes` (
  `codigo` int(11) NOT NULL,
  `nome` text NOT NULL,
  `tipo_filme` int(11) NOT NULL,
  `diretor` int(11) NOT NULL,
  `ator_principal` int(11) NOT NULL,
  `detalhes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `filmes`
--

INSERT INTO `filmes` (`codigo`, `nome`, `tipo_filme`, `diretor`, `ator_principal`, `detalhes`) VALUES
(1, 'CHAMAS DA VINGANÇA', 1, 2, 1, 'Depois de servir como cobaia para uma entidade secreta, Andy desenvolve poderes psíquicos e acaba conhecendo o amor de sua vida e tendo uma filha. O único problema é que Andy passou seus poderes para a filha, que desenvolve poderes únicos, e agora estão sendo perseguidos pela entidade novamente.');

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcoes`
--

CREATE TABLE `funcoes` (
  `codigo` int(11) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `funcoes`
--

INSERT INTO `funcoes` (`codigo`, `descricao`) VALUES
(1, 'ATOR'),
(2, 'DIRETOR'),
(3, 'PRODUTOR'),
(4, 'ROTERISTA');

-- --------------------------------------------------------

--
-- Estrutura da tabela `pessoas`
--

CREATE TABLE `pessoas` (
  `codigo` int(11) NOT NULL,
  `nome` text NOT NULL,
  `idade` int(11) DEFAULT NULL,
  `nacionalidade` text NOT NULL,
  `funcao_principal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `pessoas`
--

INSERT INTO `pessoas` (`codigo`, `nome`, `idade`, `nacionalidade`, `funcao_principal`) VALUES
(1, 'ZAC EFRON', 34, 'AMERICANO', 1),
(2, 'KEITH THOMAS (II)', NULL, 'AMERICANO', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipo_filme`
--

CREATE TABLE `tipo_filme` (
  `codigo` int(11) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `tipo_filme`
--

INSERT INTO `tipo_filme` (`codigo`, `descricao`) VALUES
(2, 'SUSPENSE');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `filmes`
--
ALTER TABLE `filmes`
  ADD PRIMARY KEY (`codigo`);

--
-- Indexes for table `funcoes`
--
ALTER TABLE `funcoes`
  ADD PRIMARY KEY (`codigo`);

--
-- Indexes for table `pessoas`
--
ALTER TABLE `pessoas`
  ADD PRIMARY KEY (`codigo`);

--
-- Indexes for table `tipo_filme`
--
ALTER TABLE `tipo_filme`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `filmes`
--
ALTER TABLE `filmes`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `funcoes`
--
ALTER TABLE `funcoes`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `pessoas`
--
ALTER TABLE `pessoas`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tipo_filme`
--
ALTER TABLE `tipo_filme`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
