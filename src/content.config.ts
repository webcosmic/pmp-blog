import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const pmpQuestions = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/pmp-questions' }),
  schema: z.object({
    title: z.string(),
    pubDate: z.coerce.date().optional(),
    topic: z.string().optional(),
    category: z.string(),
    difficulty: z.number(),
    correctAnswer: z.enum(['A', 'B', 'C', 'D']).optional(),
    slug: z.string().optional(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'pmp-questions': pmpQuestions,
};