--
-- @lc app=leetcode id=619 lang=mysql
--
-- [619] Biggest Single Number
--
-- https://leetcode.com/problems/biggest-single-number/description/
--
-- database
-- Easy (40.17%)
-- Total Accepted:    14.9K
-- Total Submissions: 37K
-- Testcase Example:  '{"headers": {"my_numbers": ["num"]}, "rows": {"my_numbers": [[8],[8],[3],[3],[1],[4],[5],[6]]}}'
--
-- Table my_numbers contains many numbers in column num including duplicated
-- ones.
-- Can you write a SQL query to find the biggest number, which only appears
-- once.
-- 
-- 
-- +---+
-- |num|
-- +---+
-- | 8 |
-- | 8 |
-- | 3 |
-- | 3 |
-- | 1 |
-- | 4 |
-- | 5 |
-- | 6 | 
-- 
-- For the sample data above, your query should return the following result:
-- 
-- 
-- +---+
-- |num|
-- +---+
-- | 6 |
-- 
-- Note:
-- If there is no such number, just output null.
-- 
-- 
-- 
--
# Write your MySQL query statement below

