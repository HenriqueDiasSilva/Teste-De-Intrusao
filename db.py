import sqlite3
import bcrypt

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


def criar_tabela():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            senha TEXT
        )
    ''')


def cadastrar_usuario(nome, email, senha):
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''
        INSERT INTO usuario (nome, email, senha)
        VALUES (?, ?, ?)
    ''', (nome, email, senha_hash))
    conn.commit()


def login_usuario(email, senha):
    cursor.execute('''
        SELECT senha FROM usuario WHERE email = ?
    ''', (email,))
    resultado = cursor.fetchone()
    if resultado and bcrypt.checkpw(senha.encode('utf-8'), resultado[0]):
        return "\nLogin bem-sucedido!"
    else:
        return "\nEmail ou senha incorretos."
