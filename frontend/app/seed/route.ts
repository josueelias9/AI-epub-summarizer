import bcrypt from 'bcrypt'
import postgres from 'postgres'
import { randomUUID } from 'crypto'

const connectionString = `postgresql://${process.env.POSTGRES_USER}:${process.env.POSTGRES_PASSWORD}@${process.env.DB_HOST}:${process.env.DB_PORT}/${process.env.POSTGRES_DB}`

const sql = postgres(connectionString, { ssl: false })

const initialUser = {
    name: 'Admin',
    email: process.env.SEED_USER_EMAIL ?? 'admin@example.com',
    password: process.env.SEED_USER_PASSWORD ?? 'password123'
}

async function seedUsers() {
    const hashedPassword = await bcrypt.hash(initialUser.password, 10)

    await sql`
        INSERT INTO users (id, name, email, password)
        VALUES (${randomUUID()}, ${initialUser.name}, ${initialUser.email}, ${hashedPassword})
        ON CONFLICT (email) DO NOTHING;
    `
}

export async function GET() {
    try {
        await seedUsers()
        return Response.json({ message: 'Database seeded successfully' })
    } catch (error) {
        return Response.json({ error: String(error) }, { status: 500 })
    }
}
