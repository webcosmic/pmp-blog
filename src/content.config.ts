import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const pmpQuestions = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/pmp-questions' }),
  schema: z.object({
    title: z.string(),
    category: z.string(),
    difficulty: z.number(),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'pmp-questions': pmpQuestions,
};