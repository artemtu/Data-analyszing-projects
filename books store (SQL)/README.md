# Books store (SQL)

Our client is an online books store. They have a database with information about books, publishing houses, authors, and user reviews.

Tasks:
- How many books were published after the 1 of January 2000
- For every book count reviews quantity and average grade
- Find a publishing house which published books with more than 50 pages
- Find authors which a high grade on the books. We should find books with more than 50 pages
- Find average user reviews which sent more than 50 reviews

**Description of the data:**

 *books*
- book_id 
- author_id
- title 
- num_pages — quantity of pages
- publication_date 
- publisher_id

*authors*
- author_id 
- author 

*publishers*
- publisher_id 
- publisher 

*ratings*
- rating_id 
- book_id 
- username 
- rating 

*reviews*
- review_id 
- book_id 
- username 
- text 

The scheme of the database: https://pastenow.ru/GRSMX




## Conclusion

1. Quantity of the books published after the 1 of January 2000 - 819
2. TOP-3 publishing houses which published  books with more than 50 pages:
 * Penguin Books - 42
 * Vintage - 31
 * Grand Central Publishing - 25
3. TOP-3 authors which a high grade on the books with more than 50 pages:
 * J.K. Rowling/Mary GrandPré	 - 4.28
 * Markus Zusak/Cao Xuân Việt Khương - 4.26
 * J.R.R. Tolkien - 4.25
4. Average user reviews which sent more than 50 reviews - 24
